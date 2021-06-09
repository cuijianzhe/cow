from django.urls import path

from asset.polardb.apis import polardb as polardb_api


urlpatterns = [
    path('polardb/', polardb_api.PolarDBApi.as_view()),
    path('polardb/list/', polardb_api.ListPolarDBApi.as_view()),
    path('polardb/sync/', polardb_api.SyncPolarDBApi.as_view()),
]
