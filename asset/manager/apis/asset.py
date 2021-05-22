from base.api import BaseApi
from asset.manager.controllers import asset as asset_ctl

class CreateAssetApi(BaseApi):
    need_params = {
        'name':('名称','required str 128'),
        'sign':('标识','required str 128'),
        'rank':('排序值','required int'),
        'remark':('备注','optional str 128'),
    }
    def post(self,request,params):
        asset_ctl.create_asset(**params)

class UpdateAssetApi(BaseApi):
    need_params = {
        'obj_id': ('资产模块ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
        'rank': ('排序值', 'required int'),
        'remark': ('备注', 'optional str'),
    }
    def post(self, request, params):
        asset_ctl.update_asset(**params)

class DeleteAssetApi(BaseApi):

    need_params = {
        'obj_id': ('资产模块ID', 'required int'),
    }
    def post(self, request, params):
        asset_ctl.delete_asset(**params)

class AssetApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('资产模块ID', 'required int'),
    }
    def get(self, request, params):
        data = asset_ctl.get_asset(**params)
        return data


class ListAssetApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = asset_ctl.get_assets(**params)
        return data
