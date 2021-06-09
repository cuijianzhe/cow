from base.api import BaseApi
from asset.polardb.controllers import account as account_ctl


class PolarDBAccountApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('账号ID', 'required int'),
    }
    def get(self, request, params):
        data = account_ctl.get_account(**params)
        return data


class ListPolarDBAccountApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'polardb_id': ('PolarDB ID', 'required int'),
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = account_ctl.get_accounts(**params)
        return data


class UpdatePolarDBAccountApi(BaseApi):

    need_params = {
        'obj_id': ('账号ID', 'required int'),
        'password': ('密码', 'required str'),
    }
    def post(self, request, params):
        account_ctl.update_account(**params)


class ListPolarDBAccountDatabaseApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('账号ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = account_ctl.get_account_databases(**params)
        return data
