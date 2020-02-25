from django.db import models

# Create your models here.

class bdd_sites(models.Model):

	nom_site = models.CharField(blank=False, default=" ", max_length=400)
	image_site = models.FileField(upload_to='image_site/',default="")
	lien_site = models.CharField(blank=False, default=" ", max_length=400)
	couleur_site = models.CharField(blank=False, default=" ", max_length=400)

	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Site"
		ordering = ['nom_site']

	def __str__(self):
		return self.nom_site