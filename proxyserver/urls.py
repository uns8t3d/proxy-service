from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import include, url
from django.contrib import admin
from proxyserver.apps.core import tools

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^', include('proxyserver.apps.authorization.urls', namespace='auth')),
    url(r'^', include('proxyserver.apps.core.urls', namespace='core')),
    url(r'^api/$', include('proxyserver.apps.api.urls')),
    url(r'^pr/$', tools.call_scrappers),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
