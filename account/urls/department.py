from django.urls import path

from account.apis import department as department_api

urlpatterns = [
    path('department/create/', department_api.CreateDepartmentApi.as_view()),
]
