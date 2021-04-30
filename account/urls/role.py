from django.urls import path

from account.apis import role as role_api

urlpatterns = [
    path('role/create/', role_api.CreateRoleApi.as_view()),
    path('role/delete/', role_api.DeleteRoleApi.as_view()),
    path('role/update/', role_api.UpdataRoleApi.as_view()),
    path('role/list/', role_api.ListRoleApi.as_view()),
    path('role/user/create/', role_api.CreateRoleUserApi.as_view()),
    path('role/user/delete/', role_api.DeleteRoleUserApi.as_view()),
    path('role/user/list/', role_api.ListRoleUserApi.as_view()),
    path('role/mod/set/', role_api.SetRoleModApi.as_view()),

]
