'''这里管理account下的所有url'''

from account.urls import user
from account.urls import department
from account.urls import role
from account.urls import mod
from account.urls import permissions
from account.urls import ldap
urlpatterns = user.urlpatterns + \
    department.urlpatterns + \
    role.urlpatterns + \
    mod.urlpatterns + \
    permissions.urlpatterns +\
    ldap.urlpatterns


