import sys
import inspect
from operator import itemgetter

import sqlobject as orm

from modules.database import models, config_models


class ClientDb:
    def __init__(self, URI="sqlite:db_sqlite.db"):
        self.connection = orm.connectionForURI(URI)
        orm.sqlhub.processConnection = self.connection

    @staticmethod
    def create_db():
        # looking for all Classes listed in models.py
        classes = [cls_name for cls_name, cls_obj
                   in inspect.getmembers(sys.modules['modules.database.models'])
                   if inspect.isclass(cls_obj)]
        for item in classes:
            # Create tables in database for each class
            # that is located in models module
            class_ = getattr(models, item)
            class_.createTable(ifNotExists=True)
        classes = [cls_name for cls_name, cls_obj
                   in inspect.getmembers(sys.modules['modules.database.config_models'])
                   if inspect.isclass(cls_obj)]
        for item in classes:
            # Create tables in database for each class
            # that is located in models module
            class_ = getattr(config_models, item)
            class_.createTable(ifNotExists=True)

    @staticmethod
    def delete_tables():
        # looking for all Classes listed in models.py
        classes = [cls_name for cls_name, cls_obj
                   in inspect.getmembers(sys.modules['modules.database.models'])
                   if inspect.isclass(cls_obj)]
        for item in classes:
            class_ = getattr(models, item)
            class_.dropTable(ifExists=True, dropJoinTables=True, cascade=True)

    @staticmethod
    def add_user(uuid, username, email=""):
        try:
            models.UserConfig(uuid=uuid,
                              username=username,
                              email=email)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add user. Error text: {error}')

    @staticmethod
    def add_flow(uuid, title):
        try:
            models.Flow(uuid=uuid,
                              title=title)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add flow. Error text: {error}')

    @staticmethod
    def add_message(uuid, text, time, userId, flowId):
        try:
            models.Message(uuid=uuid,
                           text=text,
                           time=time,
                           flow=flowId,
                           user=userId)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add flow. Error text: {error}')

    @staticmethod
    def list_flow():
        listFlow = []
        dbQuery = models.Flow.selectBy()
        for flow in dbQuery:
            secondQuery = models.Message.selectBy(flow=flow.id).orderBy("-time")
            if secondQuery.count():
                listFlow.append({'id': flow.id, 'uuid': flow.uuid, 'title': flow.title,
                                 'lastMessage': secondQuery[0].text,
                                 'lastTime': secondQuery[0].time,
                                 'count': secondQuery.count()})
            else:
                listFlow.append({'id': flow.id, 'uuid': flow.uuid, 'title': flow.title,
                                 'lastMessage': "", 'lastTime': 0, 'count': 0})
        for line in sorted(listFlow, key=itemgetter('lastTime'), reverse=True):
            yield line

    @staticmethod
    def list_messages(flow_id):
        dbQuery = models.Message.selectBy(flow=flow_id).orderBy("-time")
        for line in dbQuery:
            user = models.UserConfig.selectBy(id=line.user).getOne()
            yield {'id': line.id, 'uuid': line.uuid, 'text': line.text, 'time': line.time,
                   'userid': user.id, 'userUuid': user.uuid, 'username': user.username}

    @staticmethod
    def get_user_id_by_uuid(user_uuid):
        return models.UserConfig.selectBy(uuid=user_uuid).getOne().id

    @staticmethod
    def get_user_uuid_by_id(user_id):
        return models.UserConfig.selectBy(id=user_id).getOne().uuid

    @staticmethod
    def get_flow_id_by_uuid(flow_uuid):
        return models.Flow.selectBy(uuid=flow_uuid).getOne().id

    @staticmethod
    def get_flow_uuid_by_id(flow_id):
        return models.Flow.selectBy(id=flow_id).getOne().uuid

    @staticmethod
    def get_param(param, defaultValue=""):
        dbQuery = config_models.Config.selectBy(param=param)
        if dbQuery.count():
            return dbQuery[0].value
        else:
            return defaultValue

    @staticmethod
    def set_param(param, value):
        dbQuery = config_models.Config.selectBy(param=param)
        if dbQuery.count():
            dbQuery[0].value = value
        else:
            return config_models.Config(param=param, value=value)

    @staticmethod
    def delete_param(param):
        dbQuery = config_models.Config.selectBy(param=param)
        if dbQuery.count():
            dbQuery[0].delete(dbQuery[0].id)

