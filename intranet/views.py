from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound,Http404, JsonResponse


def index_intranet(request):
	if request.user.id == None:
		return HttpResponseRedirect('/admin/login/?next=/intranet/')

	liste_sites = bdd_sites.objects.filter(archive=False)

	context = locals()
	template = 'index_intranet.html'
	return render(request,template,context)

def statistique(request):
	
	context = locals()
	template = 'statistique.html'
	return render(request,template,context)