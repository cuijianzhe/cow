
from base.api import BaseApi
from asset.polardb.controllers import polardb as polardb_ctl


class PolarDBApi(BaseApi):
    need_params = {
        'obj_id':('PolarDB ID','required int')
    }
    def get(self,request,params):
        data = polardb_ctl.get_polardb(**params)
        return data

class ListPolarDBApi(BaseApi):
    need_params = {
        'keyword':('关键字','optional str'),
        'page_num':('页容量','optional int'),
        'page_size':('页码','optional int')
    }
    def get(self,request,params):
        data = polardb_ctl.get_polardbs(**params)
        return data

class SyncPolarDBApi(BaseApi):
    need_params = {}
    def post(self,request,params):
        polardb_ctl.sync_polardbs(**params)