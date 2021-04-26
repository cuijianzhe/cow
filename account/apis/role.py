from base.api import BaseApi
from account.controllers import role as role_ctl

class CreateRoleApi(BaseApi):
    need_params = {
        'name':('名称','required str 32'),
        'sign':('标识','required str 32')
    }
    def post(self,request,params):
        role_ctl.create_role(**params)

class DeleteRoleApi(BaseApi):
    need_params = {
        'obj_id':('角色ID','required int')
    }
    def post(self,request,params):
        role_ctl.delete_role(**params)

class UpdataRoleApi(BaseApi):
    need_params = {
        'obj_id':('角色ID','required int'),
        'name':('名称','required str 32'),
        'sign':('标识','required str 32'),
    }
    def post(self,request,params):
        role_ctl.update_role(**params)
class ListRoleApi(BaseApi):
    need_params = {
        'keyword':('关键词','required str 32'),
        'page_num':('页码','optional int'),
        'page_size':('页容量','optional int')
    }
    def get(self,request,params):
        data = role_ctl.get_roles(**params)
        return data