from base.api import BaseApi
from business.project import controllers as project_ctl


class CreateProjectApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        project_ctl.create_project(**params)

class UpdateProjectApi(BaseApi):

    need_params = {
        'obj_id': ('项目ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        project_ctl.update_project(**params)


class DeleteProjectApi(BaseApi):

    need_params = {
        'obj_id': ('项目ID', 'required int'),
    }
    def post(self, request, params):
        project_ctl.delete_project(**params)


class ListProjectApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 32'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = project_ctl.get_projects(**params)
        return data


class ProjectApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('项目ID', 'required int'),
    }

    def get(self, request, params):
        data = project_ctl.get_project(**params)
        return data

class CreateProjectUserApi(BaseApi):

    need_params = {
        'obj_id': ('项目ID', 'required int'),
        'user_id': ('用户ID', 'required int'),
        'typ': ('类型', 'required int'),
    }
    def post(self, request, params):
        project_ctl.create_project_user(**params)

class DeleteProjectUserApi(BaseApi):
    need_params = {
        'obj_id':('项目ID','required int'),
        'user_id':('用户ID','required int')
    }
    def post(self,request,params):
        project_ctl.delete_project(**params)

class UpdateProjectUserApi(BaseApi):

    need_params = {
        'obj_id': ('项目ID', 'required int'),
        'user_id': ('用户ID', 'required int'),
        'typ': ('类型', 'required int'),
    }
    def post(self, request, params):
        project_ctl.update_project_user(**params)

class ListProjectUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('项目ID', 'required int'),
        'typ': ('类型', 'optional int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = project_ctl.get_project_users(**params)
        return data