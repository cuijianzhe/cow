from base.api import BaseApi
from asset.rds.controllers import  rds as rds_ctl

class ListRdsApi(BaseApi):
    need_params = {
        'keyword':('关键字','optional str'),
        'page_num':('页容量','optional int'),
        'page_size':('页码','optional int')
    }
    def get(self,request,params):
        data = rds_ctl.get_rdses(**params)
        return data

class RdsApi(BaseApi):
    need_params = {
        'obj_id':('RDS ID','required int')
    }
    def get(self,request,params):
        data = rds_ctl.get_rds(**params)
        return data

class SyncRdsApi(BaseApi):
    need_params = {}
    def post(self,request,params):
        rds_ctl.sync_rdses(**params)