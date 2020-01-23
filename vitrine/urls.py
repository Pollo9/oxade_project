from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index_vitrine, name='index_vitrine'),


	url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
	url(r'^sitemap\.xml/$', TemplateView.as_view(template_name='sitemap.xml',content_type='text/xml')),

	url(r'^a-propos-de-nous/', views.a_propos, name='a_propos'),
	url(r'^evenements/', views.evenements, name='evenements'),
	url(r'^nous-rejoindre/', views.nous_rejoindre, name='nous_rejoindre'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^mention-legales/', views.mentions_legales, name='mentions_legales'),

	# OFFRES
	url(r'^architecture-systemes/', views.architecture, name='architecture'),
	url(r'^autres/', views.autres, name='autres'),
	url(r'^coaching/', views.coaching, name='coaching'),
	url(r'^amoa/', views.amoa, name='amoa'),
	url(r'^innovation-digitale/', views.digitalisation, name='digitalisation'),
	url(r'^securite/', views.securite, name='securite'),
	url(r'^transformation/', views.transformation, name='transformation'),
	url(r'^excellence-operationnelle/', views.excellence_operationnelle, name='excellence_operationnelle'),


	#SECTEURS
	url(r'^banque/', views.banque, name='banque'),
	url(r'^assurance/', views.assurance, name='assurance'),
	url(r'^secteur-public/', views.secteur_public, name='secteur_public'),


]
