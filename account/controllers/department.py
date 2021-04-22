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

def get_department(keyword=None, page_num=None, page_size=None, operator=None):
    base_query = DepartmentModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(sign__icontains=keyword))
        # icontains 忽略大小写  contains 大小写 icontains是表示模糊匹配, 主要还有个 contains，两者区别是是否区分大小写
        total = base_query.count()
        objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
        data_list = [obj.to_dict() for obj in objs]
        data = {
            'total':total,
            'data_list':data_list
        }
        return data

def delete_department(obj_id,operator=None):

    obj = base_ctl.get_obj(DepartmentModel,obj_id)
    base_ctl.delete_obj(DepartmentModel,obj_id,operator)