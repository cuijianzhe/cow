from django.urls import path

from asset.polardb.apis import polardb as polardb_api


urlpatterns = [
    # path('rds/', rds_api.RdsApi.as_view()),
    # path('rds/list/', rds_api.ListRdsApi.as_view()),
    path('polardb/sync/', polardb_api.SyncPolarDBApi.as_view()),
]
