from django.urls import path

from account.apis import permission as permission_api

urlpatterns = [
    path('permissions/create/', permission_api.CreatePermissions.as_view()),
    path('permissions/update/', permission_api.UpdatePermissions.as_view()),
    path('permissions/delete/', permission_api.DeletePermissions.as_view()),
    path('permissions/list/', permission_api.ListPermissionsApi.as_view()),
    path('permissions/', permission_api.PermissionApi.as_view()),

]
