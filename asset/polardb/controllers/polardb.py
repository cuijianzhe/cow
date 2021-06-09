from django.db import transaction
from django.db.models import Q

from asset.polardb.models import PolarDBModel
from scheduler.controllers import berry as berry_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl

from asset.polardb.controllers import sync as polardb_sync

def get_polardb(obj_id,operator=None):
    '''
    获取PolarDB详情
    '''
    obj = base_ctl.get_obj(PolarDBModel,obj_id)
    data = obj.to_dict()
    return data

def get_polardbs(keyword=None,page_num=None,page_size=None,operator=None):
    '''
    获取PolarDB列表
    '''
    base_query = PolarDBModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(connection__icontains=keyword)|
                                       Q(instance_id__icontains=keyword)
                                        )
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

def sync_polardbs(operator=None):
    '''
    同步PolarDB
    '''
    aliyun_key_ctl.get_enabled_aliyun_key()

    params = {}
    data = {
        'name': '同步PolarDB',
        'typ': 'sync_polardb',
        'input_params': params,
        'operator': operator,
    }
    # polardb_sync.sync_polardbs()
    berry_ctl.create_berry(**data)