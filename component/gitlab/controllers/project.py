from django.db import transaction
from django.db.models import Q

from component.gitlab.models import GitlabProjectModel

from base import controllers as base_ctl
from base import errors

def get_gitlab_projects(keyword=None,page_num=None,page_size=None,operator=None):
    '''
    获取gitlab项目列表
    '''
    base_query = GitlabProjectModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(web_url__icontains=keyword)|
                                       Q(ssh_url__icontains=keyword))
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query,page_num,page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total':total,
        'data_list':data_list,
    }
    return data
