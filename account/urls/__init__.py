'''这里管理account下的所有url'''

from account.urls import user
from account.urls import department
urlpatterns = user.urlpatterns + \
    department.urlpatterns