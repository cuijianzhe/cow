from base.api import BaseApi
from component.gitlab.controllers import server as server_ctl

class CreateGitlabServerApi(BaseApi):
    '''
    创建
    '''
    need_params = {
        'name':('名称','required str 128'),
        'host':('Host','required str 128'),
        'username':('用户名','required str 128'),
        'password':('密码','required str 128'),
        'token':('Token','required str 128'),
    }
    def post(self,request,params):
        server_ctl.creat_gitlab_server(**params)

class UpdateGitlabServerApi(BaseApi):

    need_params = {
        'obj_id': ('Gitlab服务ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'host': ('Host', 'required str 128'),
        'username': ('用户名', 'required str 128'),
        'password': ('密码', 'required str 128'),
        'token': ('Token', 'required str 128'),
    }
    def post(self, request, params):
        server_ctl.update_gitlab_server(**params)


class DeleteGitlabServerApi(BaseApi):

    need_params = {
        'obj_id': ('Gitlab服务ID', 'required int'),
    }
    def post(self, request, params):
        server_ctl.delete_gitlab_server(**params)


class ListGitlabServerApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = server_ctl.get_gitlab_servers(**params)
        return data


class GitlabServerApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Gitlab服务ID', 'required int'),
    }
    def get(self, request, params):
        data = server_ctl.get_gitlab_server(**params)
        return data