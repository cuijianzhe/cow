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