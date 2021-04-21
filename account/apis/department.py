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

