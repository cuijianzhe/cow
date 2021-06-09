from django.db import transaction
from django.db.models import Q

from asset.polardb.models import PolarDBAccountModel,PolarDBDatabaseModel,PolarDBDatabaseAccountModel

from account.controllers import user as user_ctl
from base import controllers as base_ctl
from base import errors

def get_databases(polardb_id=None, polardb_instance_id=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Database列表
    '''
    if not polardb_id and not polardb_instance_id:
        raise errors.CommonError('缺少PolarDB ID或PolarDB实例ID')
    base_query = PolarDBDatabaseModel.objects
    if polardb_id:
        base_query = base_query.filter(polardb_id=polardb_id)
    else:
        base_query = base_query.filter(polardb__instance_id=polardb_instance_id)
    if keyword:
        base_query = base_query.filter(name__icontains=keyword)
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


def get_database(obj_id, operator=None):
    '''
    获取Database详情
    '''
    obj = base_ctl.get_obj(PolarDBDatabaseModel, obj_id)
    data = obj.to_dict()
    data['rds'] = obj.rds.to_dict()
    return data

def get_database_accounts(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取Database关联账号列表
    '''
    base_query = PolarDBDatabaseAccountModel.objects.filter(database_id=obj_id)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    has_password = False
    if operator and user_ctl.has_permission(operator.id, PolarDBAccountModel.PASSWORD_PERMISSION):
        has_password = True
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['account'] = obj.account.to_dict(has_password=has_password)
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data