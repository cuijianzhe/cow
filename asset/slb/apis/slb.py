
from base.api import BaseApi
from asset.slb.controllers import slb as slb_ctl


class SyncSlbApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        slb_ctl.sync_slbs(**params)
