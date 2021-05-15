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

def update_gitlab_server(obj_id,name,host,username,password,token,operator=None):
    '''
    更新编辑gitlab服务
    '''
    if GitlabServerModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('Gitlab服务已存在')
    if GitlabServerModel.objects.filter(host=host).exclude(id=obj_id).exists():
        raise errors.CommonError('Gitlab服务已存在')
    data = {
        'name':name,
        'host':host,
        'username':username,
        'password':password,
        'token':token,
    }
    obj = base_ctl.update_obj(GitlabServerModel,obj_id,data,operator)
    data = obj.to_dict()
    return data

def delete_gitlab_server(obj_id, operator=None):
    '''
    删除Gitlab服务
    '''
    base_ctl.delete_obj(GitlabServerModel, obj_id, operator)

def get_gitlab_servers(page_num=None,page_size=None,operator=None):
    '''
    获取gitlab服务列表
    '''
    base_query = GitlabServerModel.objects
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query,page_size,page_num)
    has_password = False
    if operator and user_ctl.has_permission(operator.id,GitlabServerModel,PASSWORD_PERMISSION):
        has_password = True
    data_list = []
    for obj in objs:
        data = obj.to_dict(has_password=has_password)
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list,
    }
    return data

def get_gitlab_server(obj_id, operator=None):
    '''
    获取Gitlab服务
    '''
    obj = base_ctl.get_obj(GitlabServerModel, obj_id)
    has_password = False
    if operator and user_ctl.has_permission(operator.id, GitlabServerModel.PASSWORD_PERMISSION):
        has_password = True
    data = obj.to_dict(has_password=has_password)
    return data


