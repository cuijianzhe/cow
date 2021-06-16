from business.service.urls import service
from business.service.urls import language
from business.service.urls import frame,asset,environment

urlpatterns = service.urlpatterns +\
    language.urlpatterns +\
    frame.urlpatterns +\
    asset.urlpatterns +\
    environment.urlpatterns
