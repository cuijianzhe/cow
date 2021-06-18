from django.urls import path

from business.service.apis import polardb as polardb_api


urlpatterns = [
    path('service/polardb/create/', polardb_api.CreateServicePolarDBApi.as_view()),
    path('service/polardb/delete/', polardb_api.DeleteServicePolarDBApi.as_view()),
    path('service/polardb/list/', polardb_api.ListServicePolarDBApi.as_view()),
]
