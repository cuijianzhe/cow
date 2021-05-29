from django.db import transaction
from django.db.models import Q

from asset.slb.models import SlbModel
from scheduler.controllers import berry as berry_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl
from asset.slb.controllers import sync as slb_sync


def sync_slbs(operator=None):
    '''
    同步SLB
    '''
    # 先进行是否存在阿里云Key判断
    aliyun_key_ctl.get_enabled_aliyun_key()

    params = {}
    data = {
        'name': '同步SLB',
        'typ': 'sync_slb',
        'input_params': params,
        'operator': operator,
    }

    # slb_sync.sync_slbs()
    berry_ctl.create_berry(**data)