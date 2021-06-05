from asset.manager import urls as manager_urls
from asset.ecs import urls as ecs_urls
from asset.slb import urls as slb_urls
from asset.domain import urls as domain_urls
from asset.rds import urls as rds_urls
from asset.redis import urls as redis_urls

urlpatterns = manager_urls.urlpatterns +\
    ecs_urls.urlpatterns +\
    slb_urls.urlpatterns + \
    domain_urls.urlpatterns + \
    rds_urls.urlpatterns +\
    redis_urls.urlpatterns

