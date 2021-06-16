from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceModel
from business.service.models import ServiceEnvironmentModel
from business.service.models import EnvironmentModel
from business.service.models import DepartmentServiceModel
from business.service.models import ServiceUserModel

def create_service(name, sign, project_id, language_id, frame_id, gitlab_id, remark=None, operator=None):
    '''
    创建服务
    '''
    if ServiceModel.objects.filter(name=name).exists():
        raise errors.CommonError('服务名称已存在')
    if ServiceModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('服务标识已存在')
    data = {
        'name': name,
        'sign': sign,
        'project_id': project_id,
        'language_id': language_id,
        'frame_id': frame_id,
        'gitlab_id': gitlab_id,
        'remark': remark,
    }
    obj = base_ctl.create_obj(ServiceModel, data, operator)
    data = obj.to_dict()
    return data