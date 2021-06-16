from base.api import BaseApi
from business.service.controllers import service as service_ctl


class CreateServiceApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
        'project_id': ('项目ID', 'required int'),
        'language_id': ('编程语言ID', 'required int'),
        'frame_id': ('框架ID', 'required int'),
        'gitlab_id': ('代码库ID', 'required int'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        service_ctl.create_service(**params)