from django.db import models
from base.models import BaseModel
from business.project.models import ProjectModel
from account.models import UserModel
from account.models import DepartmentModel

class EnvironmentModel(BaseModel):
    '''
    环境
    qa/release/prod
    '''
    model_name = '环境'
    model_sign = 'environment'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    rank = models.IntegerField('排序值', default=0)
    remark = models.TextField('备注', default='', null=True)

    class Meta:
        db_table = 'environment'

class LanguageModel(BaseModel):
    '''
    编程语言
    '''
    model_name = '编程语言'
    model_sign = 'language'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)

    class Meta:
        db_table = 'language'

class FrameModel(BaseModel):
    '''
    框架
    '''
    model_name = '框架'
    model_sign = 'frame'

    language = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)

    class Meta:
        db_table = 'frame'

