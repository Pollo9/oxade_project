from django.contrib import admin
from .models import *

# Register your models here.
class bdd_sitesAdmin(admin.ModelAdmin):
	list_display = ('id','nom_site','lien_site','image_site','archive')


admin.site.register(bdd_sites,bdd_sitesAdmin)