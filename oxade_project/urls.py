from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
	#Admin
    url(r'^admin/', admin.site.urls),
    #les applicaiton include
    url(r'^', include('vitrine.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)