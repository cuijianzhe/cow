from django.urls import path

from asset.polardb.apis import database as database_api
urlpatterns = [
    path('polardb/database/list/', database_api.ListPolarDBDatabaseApi.as_view()),
    path('polardb/database/', database_api.PolarDBDatabaseApi.as_view()),
    path('polardb/database/account/list/', database_api.ListPolarDBDatabaseAccountApi.as_view())

]
