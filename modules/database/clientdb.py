import sys
import inspect
from operator import itemgetter

import sqlobject as orm

from modules.database import models

URI = "sqlite:db_sqlite.db"


class ClientDb:
    def __init__(self):
        self.connection = orm.connectionForURI(URI)
        orm.sqlhub.processConnection = self.connection

    @staticmethod
    def createdb():
        # looking for all Classes listed in models.py
        classes = [cls_name for cls_name, cls_obj
                   in inspect.getmembers(sys.modules['modules.database.models'])
                   if inspect.isclass(cls_obj)]
        for item in classes:
            # Create tables in database for each class
            # that is located in models module
            class_ = getattr(models, item)
            class_.createTable(ifNotExists=True)

    @staticmethod
    def deletetables():
        # looking for all Classes listed in models.py
        classes = [cls_name for cls_name, cls_obj
                   in inspect.getmembers(sys.modules['modules.database.models'])
                   if inspect.isclass(cls_obj)]
        for item in classes:
            class_ = getattr(models, item)
            class_.dropTable(ifExists=True, dropJoinTables=True, cascade=True)

    @staticmethod
    def adduser(uuid, username, email=""):
        try:
            models.UserConfig(uuid=uuid,
                              username=username,
                              email=email)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add user. Error text: {error}')

    @staticmethod
    def addflow(uuid, title):
        try:
            models.Flow(uuid=uuid,
                              title=title)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add flow. Error text: {error}')

    @staticmethod
    def addmessage(uuid, text, time, userId, flowId):
        try:
            models.Message(uuid=uuid,
                           text=text,
                           time=time,
                           flow=flowId,
                           user=userId)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add flow. Error text: {error}')

    @staticmethod
    def listflow():
        listFlow = []
        dbQuery = models.Flow.selectBy()
        for flow in dbQuery:
            secondQuery = models.Message.selectBy(flow=flow.id).orderBy("-time")
            if secondQuery.count():
                listFlow.append({'id': flow.id, 'uuid': flow.uuid, 'title': flow.title,
                                 'lastmessage': secondQuery[0].text,
                                 'lasttime': secondQuery[0].time,
                                 'count': secondQuery.count()})
            else:
                listFlow.append({'id': flow.id, 'uuid': flow.uuid, 'title': flow.title,
                                 'lastmessage': "", 'lasttime': 0, 'count': 0})
        for line in sorted(listFlow, key=itemgetter('lasttime'), reverse=True):
            yield line

    @staticmethod
    def listmessages(flow_id):
        dbQuery = models.Message.selectBy(flow=flow_id).orderBy("-time")
        for line in dbQuery:
            user = models.UserConfig.selectBy(id=line.user).getOne()
            yield {'id': line.id, 'uuid': line.uuid, 'text': line.text, 'time': line.time,
                   'userid': user.id, 'useruuid': user.uuid, 'username': user.username}

    @staticmethod
    def getuseridbyuuid(user_uuid):
        return models.UserConfig.selectBy(uuid=user_uuid).getOne().id

    @staticmethod
    def getuseruuidbyid(user_id):
        return models.UserConfig.selectBy(id=user_id).getOne().uuid

    @staticmethod
    def getflowidbyuuid(flow_uuid):
        return models.Flow.selectBy(uuid=flow_uuid).getOne().id

    @staticmethod
    def getflowuuidbyid(flow_id):
        return models.Flow.selectBy(id=flow_id).getOne().uuid
