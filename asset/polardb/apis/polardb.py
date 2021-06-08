
from base.api import BaseApi
from asset.polardb.controllers import polardb as polardb_ctl



class SyncPolarDBApi(BaseApi):
    need_params = {}
    def post(self,request,params):
        polardb_ctl.sync_polardbs(**params)