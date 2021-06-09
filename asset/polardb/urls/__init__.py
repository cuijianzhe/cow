from asset.polardb.urls import polardb,database,account


urlpatterns = polardb.urlpatterns +\
    database.urlpatterns +\
    account.urlpatterns