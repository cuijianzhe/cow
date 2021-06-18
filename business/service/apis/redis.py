from base.api import BaseApi
from business.service.controllers import asset_obj as asset_obj_ctl


class CreateServiceRedisApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'typ': ('资产类型', 'required str'),
        'asset_obj_id': ('Redis ID', 'required int'),
    }
    def post(self, request, params):
        asset_obj_ctl.create_service_asset_obj(**params)


class DeleteServiceRedisApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'typ': ('资产类型', 'required str'),
        'asset_obj_id': ('Redis ID', 'required int'),
    }
    def post(self, request, params):
        asset_obj_ctl.delete_service_asset_obj(**params)


class ListServiceRedisApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'typ': ('资产类型', 'required str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = asset_obj_ctl.get_service_asset_objs(**params)
        return data
