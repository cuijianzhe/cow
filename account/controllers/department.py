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

def get_departments(keyword=None, page_num=None, page_size=None, operator=None):
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
    if obj:
        base_ctl.delete_obj(DepartmentModel,obj_id,operator)

def get_department(obj_id,operator=None):
    obj = base_ctl.get_obj(DepartmentModel,obj_id)
    data = obj.to_dict()
    return data

def update_department(obj_id,name=None,sign=None,operator=None):
    if DepartmentModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('部门名称已存在')
    if DepartmentModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('部门标识已存在')
    obj = base_ctl.get_obj(DepartmentModel,obj_id)
    data = {
        'name':name,
        'sign':sign,
    }
    obj = base_ctl.update_obj(DepartmentModel,obj_id,data,operator)
    data = obj.to_dict()
    return data

def create_department_user(department_id, user_id, typ, operator=None):
    '''
    创建部门关联用户
    '''
    query = {
        'user_id': user_id,
        'department_id': department_id,
    }
    if DepartmentUserModel.objects.filter(**query).exists():
        raise errors.CommonError('用户已在此部门中')
    if not DepartmentUserModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')
    data = {
        'user_id': user_id,
        'department_id': department_id,
        'typ': typ,
    }
    obj = base_ctl.create_obj(DepartmentUserModel, data, operator)
    data = obj.to_dict()
    return data

def Update_department_user(department_id,user_id,typ,operator=None):
    query = {
        'user_id':user_id,
        'department_id':department_id,
    }
    obj = DepartmentUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未在此部门')
    if not DepartmentUserModel.check_choices('typ',typ):
        raise errors.CommonError('类型不正确')
    data = {
        'typ':typ,
    }
    obj = base_ctl.update_obj(DepartmentUserModel,obj.id,data,operator)
    data = obj.to_dict()
    return data

def Delete_department_user(department_id,user_id,operator=None):
    query = {
        'user_id':user_id,
        'department_id':department_id
    }
    obj = DepartmentUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('此用户不在此部门中')
    base_ctl.delete_obj(DepartmentUserModel,obj.id,operator)

def get_department_user(obj_id, typ=None, page_num=None, page_size=None, operator=None):
    base_query = DepartmentUserModel.objects.filter(department_id=obj_id)\
        .filter(user__is_deleted=False).select_related('user')
    '''
    使用select_related()方法一次性的把Book关联的对象都查询出来放入对象中，再次查询时就不需要再连接数据库，节省了后面查询数据库的次数和时间。
    '''
    if typ:
        base_query = base_query.filter(typ=typ)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query,page_num,page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['user'] = obj.user.to_dict()
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list,
    }
    return data