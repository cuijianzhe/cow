from base.api import BaseApi
from account.controllers import user as user_ctl


class LoginApi(BaseApi):
    need_params = {
        'username': ('用户名', 'required str 32'),
        'password': ('密码', 'required str 32'),
        'is_ldap': ('是否LDAP登录', 'required bool'),
    }
    def post(self, request, params):
        data = user_ctl.login(**params)
        return data


class UserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }

    def post(self, request, params):
        data = user_ctl.get_users(**params)
        return data


class CreateUserApi(BaseApi):
    need_params = {
        'username': ('用户名', 'required str 32'),
        'password': ('密码', 'optional str 32'),
        'name': ('姓名', 'required str 32'),
        'phone': ('手机号', 'optional str 32'),
        'email': ('邮箱', 'required str 128'),
    }
    def post(self, request, params):
        data = user_ctl.create_user(**params)
        return data

class ListUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 16'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = user_ctl.get_users(**params)
        return data

class DeleteUserApi(BaseApi):
    '''
    http://192.168.51.207:10080/api/v1/account/user/delete/
    {
    "obj_id": "6"
    }
    '''
    need_params = {
        'obj_id':('用户ID','required int')
    }
    def post(self,request,params):
        user_ctl.delete_user(**params)

class UpdateUserApi(BaseApi):
    need_params = {
        'obj_id': ('用户ID', 'required int'),
        'password': ('密码', 'optional str 32'),
        'name': ('姓名', 'required str 32'),
        'phone': ('手机号', 'optional str 32'),
        'email': ('邮箱', 'optional str 128'),
    }
    def post(self, request, params):
        user_ctl.update_user(**params)

