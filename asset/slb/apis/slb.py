
from base.api import BaseApi
from asset.slb.controllers import slb as slb_ctl

class ListSlbApi(BaseApi):
    need_params = {
        'keyword':('关键字','optional str'),
        'page_num':('页码','optional int'),
        'page_size':('页容量','optional int')
    }
    def get(self,request,params):
        data = slb_ctl.get_slbs(**params)
        return data

class SlbApi(BaseApi):
    need_params = {
        'obj_id':('SLB ID','required int')
    }
    def get(self,request,params):
        data = slb_ctl.get_slb(**params)
        return data

class SyncSlbApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        slb_ctl.sync_slbs(**params)
