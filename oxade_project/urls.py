from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
	#Admin
	url(r'^admin/', admin.site.urls),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^intranet/',include('intranet.urls')),
    
    url(r'^microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    url(r'^.well-known/microsoft-identity-association.json/$', TemplateView.as_view(template_name='microsoft-identity-association.json',content_type='text/json')),
    #les applicaiton include
]

urlpatterns += i18n_patterns(
    url(r'^', include('vitrine.urls')),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)