from business.service.urls import service
from business.service.urls import language
from business.service.urls import frame,asset,environment,ecs,database,server_group,redis
from business.service.urls import domain
from business.service.urls import config
from business.service.urls import polardb

urlpatterns = service.urlpatterns +\
    language.urlpatterns +\
    frame.urlpatterns +\
    asset.urlpatterns +\
    environment.urlpatterns +\
    ecs.urlpatterns +\
    database.urlpatterns +\
    server_group.urlpatterns +\
    redis.urlpatterns +\
    domain.urlpatterns +\
    config.urlpatterns +\
    polardb.urlpatterns
