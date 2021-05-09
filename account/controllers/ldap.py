from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import LdapConfigModel
from account.controllers import user as user_ctl

def get_ldap_config(operator):
    '''
    获取
    '''
    obj = LdapConfigModel.objects.first()
    has_password = False
    if operator and user_ctl.has_permission(operator.id, LdapConfigModel.PASSWORD_PERMISSION):
        has_password = True
    if obj:
        data = obj.to_dict(has_password=has_password)
    else:
        data = LdapConfigModel.none_to_dict()
    return data

def update_ldap_config(host, admin_dn, admin_password, member_base_dn, operator=None):
    '''
    编辑服务配置
    '''

    obj = LdapConfigModel.objects.first()
    data = {
        'host': host,
        'admin_dn': admin_dn,
        'admin_password': admin_password,
        'member_base_dn': member_base_dn,
    }
    if obj:
        obj = base_ctl.update_obj(LdapConfigModel, obj.id, data, operator)
    else:
        obj = base_ctl.create_obj(LdapConfigModel, data, operator)
    data = obj.to_dict()
    return data
