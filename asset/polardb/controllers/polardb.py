from django.db import transaction
from django.db.models import Q

from asset.rds.models import RdsModel
from scheduler.controllers import berry as berry_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl

from asset.polardb.controllers import sync as polardb_sync



def sync_polardbs(operator=None):
    '''
    同步RDS
    '''
    aliyun_key_ctl.get_enabled_aliyun_key()

    params = {}
    data = {
        'name': '同步PolarDB',
        'typ': 'sync_polardb',
        'input_params': params,
        'operator': operator,
    }
    polardb_sync.sync_polardbs()
    # berry_ctl.create_berry(**data)