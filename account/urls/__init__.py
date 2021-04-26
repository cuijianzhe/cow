'''这里管理account下的所有url'''

from account.urls import user
from account.urls import department
from account.urls import role
urlpatterns = user.urlpatterns + \
    department.urlpatterns + \
    role.urlpatterns
