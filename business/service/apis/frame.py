from base.api import BaseApi
from business.service.controllers import frame as frame_ctl


class CreateFrameApi(BaseApi):

    need_params = {
        'language_id': ('编程语言ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
    }
    def post(self, request, params):
        frame_ctl.create_frame(**params)

class UpdateFrameApi(BaseApi):

    need_params = {
        'obj_id': ('框架ID', 'required int'),
        'language_id': ('编程语言ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
    }
    def post(self, request, params):
        frame_ctl.update_frame(**params)


class DeleteFrameApi(BaseApi):

    need_params = {
        'obj_id': ('框架ID', 'required int'),
    }
    def post(self, request, params):
        frame_ctl.delete_frame(**params)


class ListFrameApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'language_id': ('编程语言ID', 'optional int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = frame_ctl.get_frames(**params)
        return data


class FrameApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('框架ID', 'required int'),
    }

    def get(self, request, params):
        data = frame_ctl.get_frame(**params)
        return data
