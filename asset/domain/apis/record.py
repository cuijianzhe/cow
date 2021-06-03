from base.api import BaseApi
from asset.domain.controllers import record as record_ctl

class ListDomainRecordApi(BaseApi):
    need_params = {
        'domain_id': ('域名ID', 'optional int'),
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self,request,params):
        data = record_ctl.get_domain_records(**params)
        return data

class DomainRecordApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('解析记录ID', 'required int'),
    }
    def get(self, request, params):
        data = record_ctl.get_domain_record(**params)
        return data