import sys
import inspect
from collections import namedtuple
from operator import attrgetter
import uuid
from loguru import logger

import sqlobject as orm

from modules.database import models, config_models


class ClientDb:
    def __init__(self, URI="sqlite:db_sqlite.db"):
        self.connection = orm.connectionForURI(URI)
        orm.sqlhub.processConnection = self.connection

    @staticmethod
    def check_db_tables_created():
        return_data = True
        classes = [cls_name for cls_name, cls_obj
                   in inspect.getmembers(sys.modules['modules.database.models'])
                   if inspect.isclass(cls_obj)]
        for item in classes:
            class_ = getattr(models, item)
            try:
                class_.select().count()
            except orm.dberrors.OperationalError:
                return_data = False

        return return_data

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
            logger.error(f'Failed to add user. Error text: {error}')

    @staticmethod
    def add_flow(uuid, title, time_created=None, flow_type=None, info=None, owner=None):
        try:
            models.Flow(uuid=uuid, title=title, timeCreated=time_created,
                        flowType=flow_type, info=info, owner=owner)
        except orm.dberrors.OperationalError as error:
            logger.error(f'Failed to add flow. Error text: {error}')

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
            logger.error(f'Failed to add message. Error text: {error}')

    @staticmethod
    def update_message(uuid, text=None,
                       file_picture=None, file_video=None, file_audio=None,
                       file_document=None, emoji=None, edited_time=None, edited_status=None):
        try:
            db_query = models.Message.selectBy(uuid=uuid).getOne()
            if text:
                db_query.text = text
            if file_picture:
                db_query.filePicture = file_picture
            if file_video:
                db_query.fileVideo = file_video
            if file_audio:
                db_query.fileAudio = file_audio
            if file_document:
                db_query.fileDocument = file_document
            if emoji:
                db_query.emoji = emoji
            if edited_time:
                db_query.editedTime = edited_time
            if edited_status:
                db_query.editedStatus = edited_status
        except orm.dberrors.OperationalError as error:
            logger.error(f'Failed to update message. Error text: {error}')

    @staticmethod
    def list_flow():
        list_flow = []
        FlowTuple = namedtuple('FlowTuple',
                               'id uuid title last_message last_time count')
        db_query = models.Flow.selectBy()
        for flow in db_query:
            second_query = models.Message.selectBy(flow=flow.id).orderBy("-time")
            if second_query.count():
                list_flow.append(FlowTuple(flow.id, flow.uuid, flow.title,
                                 second_query[0].text, second_query[0].time,
                                 second_query.count()))
            else:
                list_flow.append(FlowTuple(flow.id, flow.uuid, flow.title,
                                 "", 0, 0))
        for line in sorted(list_flow, key=attrgetter('last_time'), reverse=True):
            yield line

    @staticmethod
    def list_messages(flow_id):
        MessageTuple = namedtuple('MessageTuple',
                                  'id uuid text time user_id user_uuid username')
        db_query = models.Message.selectBy(flow=flow_id).orderBy("-time")
        for line in db_query:
            user = models.UserConfig.selectBy(id=line.user).getOne()
            yield MessageTuple(line.id, line.uuid, line.text, line.time,
                               user.id, user.uuid, user.username)

    @staticmethod
    def get_user_id_by_uuid(user_uuid):
        try:
            return models.UserConfig.selectBy(uuid=user_uuid).getOne().id
        except (orm.main.SQLObjectNotFound, orm.dberrors.OperationalError) as error:
            logger.error(f'Failed to find user by uuid: {user_uuid}. Error {error}')

    @staticmethod
    def get_user_uuid_by_id(user_id):
        try:
            return models.UserConfig.selectBy(id=user_id).getOne().uuid
        except (orm.main.SQLObjectNotFound, orm.dberrors.OperationalError) as error:
            logger.error(f'Failed to find user by id: {user_id}. Error {error}')

    @staticmethod
    def get_flow_id_by_uuid(flow_uuid):
        try:
            return models.Flow.selectBy(uuid=flow_uuid).getOne().id
        except (orm.main.SQLObjectNotFound, orm.dberrors.OperationalError) as error:
            logger.error(f'Failed to find flow by uuid: {flow_uuid}. Error {error}')

    @staticmethod
    def get_flow_uuid_by_id(flow_id):
        try:
            return models.Flow.selectBy(id=flow_id).getOne().uuid
        except (orm.main.SQLObjectNotFound, orm.dberrors.OperationalError) as error:
            logger.error(f'Failed to find flow by id: {flow_id}. Error {error}')

    @staticmethod
    def get_user(user_uuid=None, user_id=None):
        try:
            if user_id and user_uuid:
                return models.UserConfig.selectBy(uuid=user_uuid, id=user_id).getOne()
            elif user_id:
                return models.UserConfig.selectBy(id=user_id).getOne()
            elif user_uuid:
                return models.UserConfig.selectBy(uuid=user_uuid).getOne()
        except (orm.main.SQLObjectNotFound, orm.dberrors.OperationalError) as error:
            logger.error(f'Failed to find user by id, uuid: {user_id}, {user_uuid}. Error {error}')

    @staticmethod
    def get_flow(flow_uuid=None, flow_id=None):
        try:
            if flow_id and flow_uuid:
                return models.Flow.selectBy(uuid=flow_uuid, id=flow_id).getOne()
            elif flow_id:
                return models.Flow.selectBy(id=flow_id).getOne()
            elif flow_uuid:
                return models.Flow.selectBy(uuid=flow_uuid).getOne()
        except (orm.main.SQLObjectNotFound, orm.dberrors.OperationalError) as error:
            logger.error(f'Failed to find user by id, uuid: {flow_id}, {flow_uuid}. Error {error}')

    def get_last_message(self, flow_uuid):
        flow_id = self.get_flow_id_by_uuid(flow_uuid)
        list_mes = list(self.list_messages(flow_id))
        if len(list_mes):
            return list_mes[-1]
        else:
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

