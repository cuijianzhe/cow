from django.db import transaction
from asset.manager.models import AliyunKeyModel
from base import controllers as base_ctl
from base import errors

def create_aliyun_key(key,secret,operator=None):
    '''
    创建阿里云key
    '''
    if AliyunKeyModel.objects.filter(key=key).exists():
        raise errors.CommonError('此key已存在')
    data = {
        'key':key,
        'secret':secret,
    }
    obj = base_ctl.create_obj(AliyunKeyModel,data,operator)
    data = obj.to_dict()
    return data

def delete_aliyun_key(obj_id,operator=None):
    '''
    删除阿里云key
    '''
    obj = base_ctl.get_obj(AliyunKeyModel,obj_id)
    if obj.status == AliyunKeyModel.ST_ENABLE:
        raise errors.CommonError('不允许删除启用状态的key')
    base_ctl.delete_obj(AliyunKeyModel,obj_id,operator)

def get_aliyun_keys(page_num,page_size,operator=None):
    '''
    获取阿里云key列表
    '''
    base_query = AliyunKeyModel.objects
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query,page_num,page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list
    }
    return data

def get_aliyun_key(obj_id, operator=None):
    '''
    获取阿里云key
    '''
    obj = base_ctl.get_obj(AliyunKeyModel, obj_id)
    data = obj.to_dict()
    return data

def update_aliyun_key(obj_id, key, secret, operator):
    '''
    编辑阿里云key
    '''
    if AliyunKeyModel.objects.filter(key=key).exclude(id=obj_id).exists():
        raise errors.CommonError('此Key已经存在')
    data = {
        'key': key,
        'secret': secret,
    }
    obj = base_ctl.update_obj(AliyunKeyModel, obj_id, data, operator)
    data = obj.to_dict()
    return data