from django.urls import path

from account.apis import department as department_api

urlpatterns = [
    path('department/create/', department_api.CreateDepartmentApi.as_view()),
    path('department/list/', department_api.ListDepartmentApi.as_view()),
    path('department/delete/', department_api.DeleteDepartmentApi.as_view()),

]
