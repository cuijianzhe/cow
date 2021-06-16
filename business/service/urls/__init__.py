from business.service.urls import service
from business.service.urls import language
from business.service.urls import frame

urlpatterns = service.urlpatterns +\
    language.urlpatterns +\
    frame.urlpatterns