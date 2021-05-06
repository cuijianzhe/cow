from base.api import BaseApi
from account.controllers import role as role_ctl

class CreateRoleApi(BaseApi):
    '''
    创建角色
    '''
    need_params = {
        'name':('名称','required str 32'),
        'sign':('标识','required str 32')
    }
    def post(self,request,params):
        role_ctl.create_role(**params)

class DeleteRoleApi(BaseApi):
    '''
    删除角色
    '''
    need_params = {
        'obj_id':('角色ID','required int')
    }
    def post(self,request,params):
        role_ctl.delete_role(**params)

class UpdataRoleApi(BaseApi):
    '''
    更新角色
    '''
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
    '''
    创建角色关联用户
    '''
    need_params = {
        'user_id':('用户ID','required int'),
        'role_id':('角色ID','required int'),
    }
    def post(self,request,params):
        role_ctl.create_role_user(**params)

class DeleteRoleUserApi(BaseApi):
    '''
    删除角色关联用户
    '''
    need_params = {
        'user_id':('用户ID','required int'),
        'role_id':('角色ID','required int'),
    }
    def post(self,request,params):
        role_ctl.delete_role_user(**params)

class ListRoleUserApi(BaseApi):
    '''
    获取角色用户列表
    '''
    need_params = {
       'obj_id':('角色ID','required int'),
       'page_num':('页码','optional int'),
       'page_size':('页容量','optional int'),
    }
    def get(self,request,params):
        data = role_ctl.get_role_user(**params)
        return data

class SetRoleModApi(BaseApi):
    '''
    status: create/delete，代表创建或删除
    '''

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'mod_id': ('模块ID', 'required int'),
        'status': ('状态', 'required str'),
    }
    def post(self, request, params):
        role_ctl.set_role_mod(**params)

class ListRoleModApi(BaseApi):
    '''

    '''
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = role_ctl.get_role_mods(**params)
        return data

class SetRolePermissionApi(BaseApi):
    '''
    status: create/delete，代表创建或删除
    '''

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'permission_id': ('权限ID', 'required int'),
        'status': ('状态', 'required str'),
    }
    def post(self, request, params):
        role_ctl.set_role_permission(**params)


class ListRolePermissionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = role_ctl.get_role_permissions(**params)
        return data


class RoleModPermissionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
    }

    def get(self, request, params):
        data = role_ctl.get_role_mod_permission(**params)
        return data
