import ujson as json
from django.db import transaction
from asset.polardb.models import PolarDBModel
from asset.polardb.models import PolarDBAccountModel
from asset.polardb.models import PolarDBDatabaseModel
from asset.polardb.models import PolarDBDatabaseAccountModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.time_utils import str2datetime_by_format
from utils.aliyun import AliyunPolarDB


def format_polardb_data(data):
    '''
    格式化PolarDB返回数据
    '''
    instance_id = data.get('DBClusterId')
    name = data.get('DBClusterDescription') #描述
    db_net_typ = data.get('DBClusterNetworkType') #网络类型 VPC
    db_typ = data.get('DBType') #数据库类型 mysql
    typ = data.get('Engine') #数据库 内核
    version = data.get('DBVersion')
    zone_id = data.get('ZoneId')
    region_id = data.get('RegionId')
    DBNodeNumber = data.get('DBNodeNumber') #polarDB节点
    DBNodeClass = data.get('DBNodeClass') #节点配置

    result = {
        'name': name,
        'instance_id': instance_id,
        'db_net_typ': db_net_typ,
        'db_typ': db_typ,
        'typ': typ,
        'version': version,
        'zone_id': zone_id,
        'region_id': region_id,
        'DBNodeNumber':DBNodeNumber,
        'DBNodeClass':DBNodeClass,
    }
    return result

def sync_polardbs():
    '''
    同步PolarDB
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的PolarDB，用于之后删除已经不存在的使用
        old_ids = PolarDBModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的PolarDB
        existed_ids = []
        # 记录需要新创建的PolarDB信息，用于批量创建
        polardb_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunPolarDB(key, secret, 'cn-beijing')
        for region in regions:
            region_id = region.get('instance_id')
            ali_cli.reset_region(region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                }
                data = ali_cli.get_polardbs(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_polardb_data(data)
                    instance_id = data.get('instance_id')
                    net_address = ali_cli.get_polardb_connection(instance_id)
                    if net_address:
                        data['connection'] = net_address
                    obj = PolarDBModel.objects.filter(instance_id=instance_id).first()
                    if obj:
                        base_ctl.update_obj(PolarDBModel, obj.id, data)
                        existed_ids.append(obj.id)
                    else:
                        polardb_list.append(data)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(PolarDBModel, polardb_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(PolarDBModel, deleted_ids)
    sync_polardb_accounts()

def sync_polardb_accounts():
    '''
    同步PolarDB账号
    '''
    with transaction.atomic():
        polardb_objs = PolarDBModel.objects.all()
        old_ids = PolarDBAccountModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        account_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunPolarDB(key, secret, 'cn-beijing')
        for polardb_obj in polardb_objs:
            ali_cli.reset_region(polardb_obj.region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                    'instance_id': polardb_obj.instance_id,
                }
                data = ali_cli.get_polardb_accounts(**query)
                data_list = data.get('data_list')
                for data in data_list:
                    username = data.get('AccountName')
                    query = {
                        'polardb_id': polardb_obj.id,
                        'username': username,
                    }
                    obj = PolarDBAccountModel.objects.filter(**query).first()
                    data = query
                    if not obj:
                        account_list.append(data)
                    else:
                        base_ctl.update_obj(PolarDBAccountModel, obj.id, data)
                        existed_ids.append(obj.id)
                if page_size > len(data_list):
                    break
                page_num += 1
        base_ctl.create_objs(PolarDBAccountModel, account_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(PolarDBAccountModel, deleted_ids)
    sync_polardb_databases()

def sync_polardb_databases():
    '''
    同步PolarDB Database
    '''
    with transaction.atomic():
        polardb_objs = PolarDBModel.objects.all()
        old_ids = PolarDBDatabaseModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        database_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunPolarDB(key, secret, 'cn-beijing')
        for polardb_obj in polardb_objs:
            ali_cli.reset_region(polardb_obj.region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                    'instance_id': polardb_obj.instance_id,
                }
                data = ali_cli.get_polardb_database(**query)
                data_list = data.get('data_list')
                for data in data_list:
                    instance_id = data.get('DBName')
                    name = data.get('DBName')
                    desc = data.get('DBDescription')
                    # 这里先存一下关联account信息，之后省得再用接口获取
                    accounts = data.get('Accounts').get('Account')
                    query = {
                        'polardb_id': polardb_obj.id,
                        'instance_id': instance_id,
                    }
                    obj = PolarDBDatabaseModel.objects.filter(**query).first()
                    data = query
                    data['name'] = name
                    data['desc'] = desc
                    data['accounts'] = json.dumps(accounts)
                    if not obj:
                        database_list.append(data)
                    else:
                        base_ctl.update_obj(PolarDBDatabaseModel, obj.id, data)
                        existed_ids.append(obj.id)
                if page_size > len(data_list):
                    break
                page_num += 1
        base_ctl.create_objs(PolarDBDatabaseModel, database_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(PolarDBDatabaseModel, deleted_ids)