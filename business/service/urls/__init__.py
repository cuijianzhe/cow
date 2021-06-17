from business.service.urls import service
from business.service.urls import language
from business.service.urls import frame,asset,environment,ecs,database,server_group

urlpatterns = service.urlpatterns +\
    language.urlpatterns +\
    frame.urlpatterns +\
    asset.urlpatterns +\
    environment.urlpatterns +\
    ecs.urlpatterns +\
    database.urlpatterns +\
    server_group.urlpatterns
