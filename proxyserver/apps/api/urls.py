from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'proxies', views.ProxyViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get_proxy/$', login_required(views.UserProxyList.as_view())),
]
