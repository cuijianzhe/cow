from asset.rds.urls import rds,database,account


urlpatterns = rds.urlpatterns +\
    database.urlpatterns +\
    account.urlpatterns