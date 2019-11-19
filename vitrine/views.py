from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound,Http404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def index_vitrine(request):
	context = locals()
	template = 'index_vitrine.html'
	return render(request,template,context)

def contact(request):
	context = locals()
	template = 'contact.html'
	return render(request,template,context)

def conduite_du_changement(request):
	context = locals()
	template = 'offres/conduite_du_changement.html'
	return render(request,template,context)

def evenements(request):
	context = locals()
	template = 'evenements.html'
	return render(request,template,context)

def digitalisation(request):
	context = locals()
	template = 'offres/digitalisation.html'
	return render(request,template,context)

def experience_client(request):
	context = locals()
	template = 'offres/experience_client.html'
	return render(request,template,context)

def fusions_et_acquisitions(request):
	context = locals()
	template = 'offres/fusions_et_acquisitions.html'
	return render(request,template,context)

def gestion_de_projets(request):
	context = locals()
	template = 'offres/gestion_de_projets.html'
	return render(request,template,context)

def reglementaire(request):
	context = locals()
	template = 'offres/reglementaire.html'
	return render(request,template,context)

def securite(request):
	context = locals()
	template = 'offres/securite.html'
	return render(request,template,context)

def transformation(request):
	context = locals()
	template = 'offres/transformation.html'
	return render(request,template,context)


def mentions_legales(request):
	context = locals()
	template = 'mentions_legales.html'
	return render(request,template,context)

def banque(request):
	context = locals()
	template = 'secteurs/banque.html'
	return render(request,template,context)

def assurance(request):
	context = locals()
	template = 'secteurs/assurance.html'
	return render(request,template,context)

def energie(request):
	context = locals()
	template = 'secteurs/energie.html'
	return render(request,template,context)

def secteur_public(request):
	context = locals()
	template = 'secteurs/secteur_public.html'
	return render(request,template,context)

def telecommunications(request):
	context = locals()
	template = 'secteurs/telecommunications.html'
	return render(request,template,context)

def transport_et_logistique(request):
	context = locals()
	template = 'secteurs/transport_et_logistique.html'
	return render(request,template,context)

def a_propos(request):
	context = locals()
	template = 'a_propos.html'
	return render(request,template,context)


def nous_rejoindre(request):
	context = locals()
	template = 'nous_rejoindre.html'
	return render(request,template,context)


