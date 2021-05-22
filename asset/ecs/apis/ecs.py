from base.api import BaseApi
from asset.ecs.controllers import ecs as ecs_ctl


class ListEcsApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = ecs_ctl.get_ecses(**params)
        return data