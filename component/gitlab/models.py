from django.db import models
from base.models import BaseModel

class GitlabServerModel(BaseModel):
    '''
    Gitlab服务
    '''
    model_name = 'Gitlab服务'
    model_sign = 'gitlab_server'

    # 是否可以查看密码权限
    # 如果拥有编辑权限，则必须给查看密码权限
    PASSWORD_PERMISSION = 'gitlab-account-password'

    name = models.CharField('名称', max_length=128)
    host = models.CharField('地址', max_length=128)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    # 此token为username用户登录后，头像->Settings->Access Tokens生成的
    # 专门用来调用api使用，所以生成时注意选上api
    token = models.CharField('认证token', max_length=128)

    class Meta:
        db_table = 'gitlab_server'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password:
            data['password'] = '******'
            data['to_dict'] = '******'
        return data


class GitlabProjectModel(BaseModel):
    '''
    Gitlab代码库
    '''
    model_name = 'Gitlab代码库'
    model_sign = 'gitlab_project'

    server = models.ForeignKey(GitlabServerModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    project_id = models.IntegerField('项目ID')
    web_url = models.TextField('访问url')
    ssh_url = models.TextField('ssh地址')

    class Meta:
        db_table = 'gitlab_project'
