from django.shortcuts import render, redirect

def index_intranet(request):
	
	context = locals()
	template = 'index_intranet.html'
	return render(request,template,context)