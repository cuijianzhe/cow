from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import ModModel,PermissionModel
from account.controllers import permission as permissions_ctl

def create_mod(name,sign,rank,operator=None):
    if ModModel.objects.filter(name=name).exists():
        raise errors.CommonError('名字已存在')
    if ModModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('标识已存在')
    data = {
        'name':name,
        'sign':sign,
        'rank':rank,
    }
    obj = base_ctl.create_obj(ModModel,data,operator)
    data = obj.to_dict()
    return data

def update_mod(obj_id,name,sign,rank,operator=None):
    if ModModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('名称已存在')
    if ModModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('标识已存在')
    obj = base_ctl.get_obj(ModModel,obj_id)
    data = {
        'name':name,
        'sign':sign,
        'rank':rank,
    }
    obj = base_ctl.update_obj(ModModel,obj_id,data,operator)
    data = obj.to_dict()
    return data

def delete_mod(obj_id,operator=None):
    base_ctl.delete_obj(ModModel,obj_id,operator)

def get_mods(keyword=None,need_permission=False, page_num=None, page_size=None, operator=None):
    base_query = ModModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(sign__icontains=keyword))
    total = base_query.count()
    base_query = base_query.order_by('-rank','id')
    objs = base_ctl.query_objs_by_page(base_query,page_num,page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['op_permissions'] = permissions_ctl.get_permissions(obj.id,PermissionModel.TYP_OP).get('data_list')
        data['data_permissions'] = permissions_ctl.get_permissions(obj.id,PermissionModel.TYP_DATA).get('data_list')
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list,
    }
    return data

def get_mod(obj_id, operator=None):
    '''
    获取模块
    '''
    obj = base_ctl.get_obj(ModModel, obj_id)
    data = obj.to_dict()
    return data