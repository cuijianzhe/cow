from django.db import transaction
from django.db.models import Q
from base import errors
from base import controllers as base_ctl
from account.models import DepartmentModel
from account.models import DepartmentUserModel

def create_department(name,sign,operator=None):
    if DepartmentModel.objects.filter(name=name).exists():
        raise errors.CommonError('部门已存在')
    if DepartmentModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('当前部门标识符已存在')
    data = {
        'name':name,
        'sign':sign,
    }
    obj = base_ctl.create_obj(DepartmentModel,data,operator)
    data = obj.to_dict()
    return data



