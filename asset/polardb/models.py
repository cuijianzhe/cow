from django.db import models
from base.models import BaseModel


class PolarDBModel(BaseModel):
    '''
    数据库实例
    '''
    model_name = 'POLARDB'
    model_sign = 'polardb'

    DB_NET_TYP_INTERNET = 'Internet'
    DB_NET_TYP_INTRANET = 'Intranet'
    DB_NET_TYP_CHOICES = (
        (DB_NET_TYP_INTERNET, '外网'),
        (DB_NET_TYP_INTRANET, '内网'),
    )

    # name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    name = models.TextField('备注', default='', null=True)
    db_net_typ = models.CharField('内网/外网', max_length=128, choices=DB_NET_TYP_CHOICES)
    db_typ = models.CharField('主从类型', max_length=128)
    typ = models.CharField('数据库类型', max_length=128)
    version = models.CharField('数据库版本', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    region_id = models.CharField('地域', max_length=128)
    DBNodeNumber = models.CharField('节点数量',max_length=128)
    DBNodeClass = models.CharField('节点配置',max_length=128)

    connection = models.CharField('连接字符串', max_length=512)


    class Meta:
        db_table = 'polardb'

    @property
    def web_url(self):
        host = 'https://polardb.console.aliyun.com'
        url = f'{host}/{self.region_id}/cluster/{self.instance_id}/basicInfo'
        return url

    def to_dict(self):
        data = super().to_dict()
        data['web_url'] = self.web_url
        return data


class PolarDBAccountModel(BaseModel):
    '''
    数据库账号
    '''
    model_name = 'POLARDB账号'
    model_sign = 'polardb_account'

    # 是否可以查看数据库密码权限
    # 如果拥有编辑权限，则必须给查看密码权限
    PASSWORD_PERMISSION = 'polardb-account-password'

    polardb = models.ForeignKey(PolarDBModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)

    class Meta:
        db_table = 'polardb_account'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password:
            data['password'] = '******'
        return data


class PolarDBDatabaseModel(BaseModel):
    '''
    数据库实例下的库
    '''
    model_name = '数据库实例'
    model_sign = 'polardb_database'

    polardb = models.ForeignKey(PolarDBModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    desc = models.TextField('描述')
    accounts = models.TextField('账号相关信息', default='', null=True)

    class Meta:
        db_table = 'polardb_database'

    def to_dict(self, is_base=True):
        data = super().to_dict()
        if not is_base:
            data['polardb'] = self.polardb.to_dict()
        return data


class PolarDBDatabaseAccountModel(BaseModel):
    '''
    数据库实例账号
    '''
    model_name = '数据库实例账号'
    model_sign = 'polardb_database_account'

    database = models.ForeignKey(PolarDBDatabaseModel, on_delete=models.CASCADE)
    account = models.ForeignKey(PolarDBAccountModel, on_delete=models.CASCADE)
    privilege = models.CharField('权限', max_length=128)

    class Meta:
        db_table = 'polardb_database_account'
