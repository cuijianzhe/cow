from base.api import BaseApi
from asset.domain.controllers import domain as domain_ctl

class ListDomainApi(BaseApi):
    need_params = {
        'keyword':('关键字','optional str'),
        'page_num':('页码','optional int'),
        'page_size':('页容量','optional int')
    }
    def get(self,request,params):
        data = domain_ctl.get_domains(**params)
        return data

class DomainApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Domain ID', 'required int'),
    }
    def get(self, request, params):
        data = domain_ctl.get_domain(**params)
        return data


class SyncDomainApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        domain_ctl.sync_domains(**params)
