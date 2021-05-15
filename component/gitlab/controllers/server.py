from django.db import transaction

from component.gitlab.models import GitlabServerModel
from account.controllers import user as user_ctl
from base import controllers as base_ctl
from base import errors

def creat_gitlab_server(name,host,username,password,token,operator=None):
    '''
    创建gitlab服务
    '''
    if GitlabServerModel.objects.filter(name=name).exists():
        raise errors.CommonError('Gitlab已存在')
    if GitlabServerModel.objects.filter(host=host).exists():
        raise errors.CommonError('Gitlab已存在')
    data = {
        'name':name,
        'host':host,
        'username':username,
        'password':password,
        'token':token,
    }
    obj = base_ctl.create_obj(GitlabServerModel,data,operator)
    data = obj.to_dict()
    return data