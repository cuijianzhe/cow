from business.service.urls import service
from business.service.urls import language

urlpatterns = service.urlpatterns +\
    language.urlpatterns