from base.api import BaseApi
from account.controllers import department as department_ctl

class CreateDepartmentApi(BaseApi):
    NEED_LOGIN = False
    need_params = {
        'name': ('名称','required str 16'),
        'sign': ('标识','required str 32'),
    }
    def post(self,request,params):
        department_ctl.create_department(**params)

class ListDepartmentApi(BaseApi):
    NEED_LOGIN = False
    need_params = {
        'keyword': ('关键词', 'optional str 32'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self,request,params):
        data = department_ctl.get_department(**params)
        return data

class DeleteDepartmentApi(BaseApi):
    NEED_LOGIN = False
    need_params = {
        "obj_id": ('部门ID','required int'),
    }
    def post(self,request,params):
        department_ctl.delete_department(**params)
