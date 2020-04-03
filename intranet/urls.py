from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index_intranet, name='index_intranet'),
		url(r'^statistique', views.statistique, name='statistique'),
		]