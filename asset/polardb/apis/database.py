from base.api import BaseApi
from asset.polardb.controllers import database as database_ctl

class ListPolarDBDatabaseApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'polardb_id': ('PolarDB ID', 'optional int'),
        'polardb_instance_id': ('PolarDB实例ID', 'optional str'),
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = database_ctl.get_databases(**params)
        return data

class PolarDBDatabaseApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Database ID', 'required int'),
    }
    def get(self, request, params):
        data = database_ctl.get_database(**params)
        return data


class ListPolarDBDatabaseAccountApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Database ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = database_ctl.get_database_accounts(**params)
        return data
