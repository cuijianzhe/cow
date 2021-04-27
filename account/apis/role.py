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
    '''
    获取角色列表
    '''
    need_params = {
        'keyword':('关键词','required str 32'),
        'page_num':('页码','optional int'),
        'page_size':('页容量','optional int')
    }
    def get(self,request,params):
        data = role_ctl.get_roles(**params)
        return data
def get_role(obj_id, operator=None):
    '''
    获取角色信息
    '''
    obj = base_ctl.get_obj(RoleModel, obj_id)
    data = obj.to_dict()
    return data

class CreateRoleUserApi(BaseApi):
    need_params = {
        'user_id':('用户ID','required int'),
        'role_id':('角色ID','required int'),
    }
    def post(self,request,params):
        role_ctl.create_role_user(**params)

class DeleteRoleUserApi(BaseApi):
    need_params = {
        'user_id':('用户ID','required int'),
        'role_id':('角色ID','required int'),
    }
    def post(self,request,params):
        role_ctl.delete_role_user(**params)

class ListRoleUserApi(BaseApi):
    need_params = {
       'obj_id':('角色ID','required int'),
       'page_num':('页码','optional int'),
       'page_size':('页容量','optional int'),
    }
    def get(self,request,params):
        data = role_ctl.get_role_user(**params)
        return data