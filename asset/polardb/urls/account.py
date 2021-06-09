from django.urls import path

from asset.polardb.apis import account as account_api

urlpatterns = [
    path('polardb/account/',account_api.PolarDBAccountApi.as_view()),
    path('polardb/account/list/', account_api.ListPolarDBAccountApi.as_view()),
    path('polardb/account/update/',account_api.UpdatePolarDBAccountApi.as_view()),
    path('polardb/account/database/list/',account_api.ListPolarDBAccountDatabaseApi.as_view())
]

