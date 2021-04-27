from django.db.models import Q
from django.db import transaction

from base import errors
from base import controllers as base_ctl
from account.models import RoleModel
from account.models import RoleUserModel

def create_role(name,sign,operator=None):
    obj = RoleModel.objects.filter(name=name).first()
    if obj:
        errors.CommonError('此角色已存在')
    obj = RoleModel.objects.filter(sign=sign).first()
    if obj:
        errors.CommonError('此标识已存在')
    data = {
        'name':name,
        'sign':sign,
    }
    obj = base_ctl.create_obj(RoleModel,data,operator)
    data = obj.to_dict()
    return data

def delete_role(obj_id,operator=None):
    obj = base_ctl.get_obj_or_none(RoleModel,obj_id)
    if not obj:
        raise errors.CommonError('角色不存在')
    if obj.sign == "admin":
        raise errors.CommonError('admin角色不允许删除')
    base_ctl.delete_obj(RoleModel,obj_id,operator)

def update_role(obj_id,name,sign,operator=None):
    obj = RoleModel.objects.filter(name=name).exclude(id=obj_id).first()
    if obj:
        raise errors.CommonError('角色名已存在')
    obj = RoleModel.objects.filter(sign=sign).exclude(sign=sign).first()
    if obj:
        raise errors.CommonError('标识已存在')
    obj = base_ctl.get_obj_or_none(RoleModel,obj_id)
    if not obj:
        raise errors.CommonError('角色不存在')
    if obj.sign == 'admin':
        raise errors.CommonError('admin角色不允许编辑更新')

    data = {
        'name':name,
        'sign':sign,
    }
    obj = base_ctl.update_obj(RoleModel,obj_id,data,operator)
    data = obj.to_dict()
    return data

def get_roles(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取角色列表
    '''
    base_query = RoleModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(sign__icontains=keyword))
        total = base_query.count()
        objs = base_ctl.query_objs_by_page(base_query,page_num,page_size)
        data_list = [obj.to_dict() for obj in objs]
        data = {
            'total':total,
            'data_list':data_list
        }
        return data

def get_role(obj_id, operator=None):
    '''
    获取角色信息
    '''
    obj = base_ctl.get_obj(RoleModel, obj_id)
    data = obj.to_dict()
    return data

def create_role_user(role_id,user_id,operator=None):
    '''
    创建用户角色关联
    '''
    query = {
        'user_id':user_id,
        'role_id':role_id,
    }
    if RoleUserModel.objects.filter(**query).exists():
        raise errors.CommonError('此用户已关联此角色')
    data = query
    obj = base_ctl.create_obj(RoleUserModel,data,operator)
    data = obj.to_dict()
    return data
def delete_role_user(role_id,user_id,operator=None):
    '''
    删除角色关联用户
    '''
    query = {
        'user_is':user_id,
        'role_id':role_id,
    }
    obj = RoleUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未关联此角色')
    base_ctl.delete_obj(RoleUserModel,obj.id,operator)

def get_role_user(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取角色用户列表
    '''
    base_query = RoleUserModel.objects.filter(role_id=obj_id)\
        .filter(user__is_deleted=False).select_related('user')
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query,page_size,page_num)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['user'] = obj.user.to_dict()
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list,
    }
    return data
