from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import include, url
from django.contrib import admin
from proxyserver.apps.authorization import views
from proxyserver.apps.core import views as core_views, tools
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^$', login_required(core_views.main_page)),
    url(r'^ajax_get_proxy_list/$', core_views.ajax_get_proxy_list),
    url(r'^ajax_get_country_list/$', core_views.ajax_get_country_list),
    url(r'^api/', include('proxyserver.apps.api.urls')),
    url(r'^pr/$', tools.call_scrappers),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
