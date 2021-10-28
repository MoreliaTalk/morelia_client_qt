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
    def add_user(uuid, username, email="", avatar=None, bio=None, is_bot=None):
        try:
            models.UserConfig(uuid=uuid, username=username, email=email,
                              avatar=avatar, bio=bio, isBot=is_bot)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add user. Error text: {error}')

    @staticmethod
    def add_flow(uuid, title, time_created=None, flow_type=None, info=None, owner=None):
        try:
            models.Flow(uuid=uuid, title=title, timeCreated=time_created,
                        flowType=flow_type, info=info, owner=owner)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add flow. Error text: {error}')

    @staticmethod
    def add_message(uuid, text, time, user_id, flow_id,
                    file_picture=None, file_video=None, file_audio=None,
                    file_document=None, emoji=None, edited_time=None, edited_status=None):
        try:
            models.Message(uuid=uuid,
                           text=text,
                           time=time,
                           flow=flow_id,
                           user=user_id,
                           filePicture=file_picture,
                           fileVideo=file_video,
                           fileAudio=file_audio,
                           fileDocument=file_document,
                           emoji=emoji,
                           editedTime=edited_time,
                           editedStatus=edited_status)
        except orm.dberrors.OperationalError as error:
            print(f'Failed to add flow. Error text: {error}')

    @staticmethod
    def list_flow():
        list_flow = []
        db_query = models.Flow.selectBy()
        for flow in db_query:
            second_query = models.Message.selectBy(flow=flow.id).orderBy("-time")
            if second_query.count():
                list_flow.append({'id': flow.id, 'uuid': flow.uuid, 'title': flow.title,
                                  'last_message': second_query[0].text,
                                  'last_time': second_query[0].time,
                                  'count': second_query.count()})
            else:
                list_flow.append({'id': flow.id, 'uuid': flow.uuid, 'title': flow.title,
                                  'last_message': "", 'last_time': 0, 'count': 0})
        for line in sorted(list_flow, key=itemgetter('last_time'), reverse=True):
            yield line

    @staticmethod
    def list_messages(flow_id):
        db_query = models.Message.selectBy(flow=flow_id).orderBy("-time")
        for line in db_query:
            user = models.UserConfig.selectBy(id=line.user).getOne()
            yield {'id': line.id, 'uuid': line.uuid, 'text': line.text, 'time': line.time,
                   'userid': user.id, 'user_uuid': user.uuid, 'username': user.username}

    @staticmethod
    def get_user_id_by_uuid(user_uuid):
        try:
            return models.UserConfig.selectBy(uuid=user_uuid).getOne().id
        except orm.main.SQLObjectNotFound:
            return None
        except orm.dberrors.OperationalError:
            return None

    @staticmethod
    def get_user_uuid_by_id(user_id):
        try:
            return models.UserConfig.selectBy(id=user_id).getOne().uuid
        except orm.main.SQLObjectNotFound:
            return None
        except orm.dberrors.OperationalError:
            return None

    @staticmethod
    def get_flow_id_by_uuid(flow_uuid):
        try:
            return models.Flow.selectBy(uuid=flow_uuid).getOne().id
        except orm.main.SQLObjectNotFound:
            return None
        except orm.dberrors.OperationalError:
            return None

    @staticmethod
    def get_flow_uuid_by_id(flow_id):
        try:
            return models.Flow.selectBy(id=flow_id).getOne().uuid
        except orm.main.SQLObjectNotFound:
            return None
        except orm.dberrors.OperationalError:
            return None

    @staticmethod
    def get_user(user_uuid=None, user_id=None):
        try:
            if user_id and user_uuid:
                return models.UserConfig.selectBy(uuid=user_uuid, id=user_id).getOne()
            elif user_id:
                return models.UserConfig.selectBy(id=user_id).getOne()
            elif user_uuid:
                return models.UserConfig.selectBy(uuid=user_uuid).getOne()
            else:
                return None
        except orm.main.SQLObjectNotFound:
            return None
        except orm.dberrors.OperationalError:
            return None

    @staticmethod
    def get_flow(flow_uuid=None, flow_id=None):
        try:
            if flow_id and flow_uuid:
                return models.Flow.selectBy(uuid=flow_uuid, id=flow_id).getOne()
            elif flow_id:
                return models.Flow.selectBy(id=flow_id).getOne()
            elif flow_uuid:
                return models.Flow.selectBy(uuid=flow_uuid).getOne()
            else:
                return None
        except orm.main.SQLObjectNotFound:
            return None
        except orm.dberrors.OperationalError:
            return None

    @staticmethod
    def get_param(param, default_value=""):
        db_query = config_models.Config.selectBy(param=param)
        if db_query.count():
            return db_query[0].value
        else:
            return default_value

    @staticmethod
    def set_param(param, value):
        db_query = config_models.Config.selectBy(param=param)
        if db_query.count():
            db_query[0].value = value
        else:
            return config_models.Config(param=param, value=value)

    @staticmethod
    def delete_param(param):
        db_query = config_models.Config.selectBy(param=param)
        if db_query.count():
            db_query[0].delete(db_query[0].id)

