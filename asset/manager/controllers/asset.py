from django.db import transaction
from asset.manager.models import AssetModel
from base import controllers as base_ctl
from base import errors

def create_asset(name,sign,rank,remark='',operator=None):
    '''
    创建资产模块
    '''
    if AssetModel.objects.filter(name=name).exists():
        raise errors.CommonError('资产模块已存在')
    if AssetModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('资产模块标识已存在')
    data = {
        'name':name,
        'sign':sign,
        'rank':rank,
        'remark':remark,
    }
    obj = base_ctl.create_obj(AssetModel,data,operator)
    data = obj.to_dict()
    return data

def update_asset(obj_id,name,sign,rank,remark='',operator=None):
    '''
    编辑资产模块
    '''
    if AssetModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('资产模块已存在')
    if AssetModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('资产模块标识已存在')
    data = {
        'name': name,
        'sign': sign,
        'rank': rank,
        'remark': remark,
    }
    obj = base_ctl.update_obj(AssetModel, obj_id, data, operator)
    data = obj.to_dict()
    return data

def delete_asset(obj_id, operator=None):
    '''
    删除资产模块
    '''
    base_ctl.delete_obj(AssetModel, obj_id, operator)

def get_assets(page_num,page_size,operator=None):
    '''
    获取资产模块
    '''
    base_query = AssetModel.objects
    total = base_query.count()
    base_query = base_query.order_by('-rank')
    objs = base_ctl.query_objs_by_page(base_query,page_num,page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list,
    }
    return data

def get_asset(obj_id, operator=None):
    '''
    获取资产详情
    '''
    obj = base_ctl.get_obj(AssetModel, obj_id)
    data = obj.to_dict()
    return data
