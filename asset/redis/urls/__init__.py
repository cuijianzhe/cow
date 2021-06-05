from asset.redis.urls import redis,account

urlpatterns = redis.urlpatterns +\
    account.urlpatterns