from django.db import transaction
from django.db.models import Q
from asset.ecs.models import EcsModel
from base import controllers as base_ctl
from base import errors
from asset.manager.controllers import aliyun_key as aliyun_key_ctl


def get_ecses(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取ECS列表
    '''
    base_query = EcsModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(hostname__icontains=keyword) |
                                       Q(inner_ip__icontains=keyword) |
                                       Q(instance_id__icontains=keyword))
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
