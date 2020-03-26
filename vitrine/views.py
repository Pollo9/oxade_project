from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound,Http404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import *

def all_static(request):
	
	context = locals()
	template = 'all_static.html'
	return render(request,template,context)

def index_vitrine(request):
	reseaux = Bdd_reseaux.objects.all()
	evenement = Bdd_evenement.objects.all().reverse()[0]
	chiffre = Bdd_chiffre.objects.all()
	chiffre_en = Bdd_chiffre_anglais.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'index_vitrine.html'
	return render(request,template,context)

def contact(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get('envoyer'):
		Nom =  request.POST.get('nom') + " " + request.POST.get('prenom')
		commentaire =  request.POST.get('message')
		tel = request.POST.get('tel')
		titre = request.POST.get('titre')
		subject = titre + " - Oxade contact"
		emailFrom = request.POST.get('mail')


		message ='%s, \n\n%s \n\nNom/prénom : %s\nEmail : %s\nTéléphone : %s\n' %(titre, commentaire, Nom, emailFrom,tel)
		emailTo =[settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		
	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))
	context = locals()

	template = 'contact.html'
	return render(request,template,context)

def architecture(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/architecture.html'
	return render(request,template,context)

def autres(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/autres.html'
	return render(request,template,context)

def coaching(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/coaching.html'
	return render(request,template,context)

def amoa(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context= locals()
	template = 'offres/amoa.html'

	return render(request,template,context)

def pca(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context= locals()
	template = 'offres/pca.html'
	return render(request,template,context)

def evenements(request):	
	events = Bdd_evenement.objects.all().reverse()
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))


	context = locals()
	template = 'evenements.html'
	return render(request,template,context)

def digitalisation(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/digitalisation.html'
	return render(request,template,context)

def securite(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/securite.html'
	return render(request,template,context)

def transformation(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/transformation.html'
	return render(request,template,context)

def excellence_operationnelle(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/excellence_operationnelle.html'
	return render(request,template,context)


def mentions_legales(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'mentions_legales.html'
	return render(request,template,context)

def banque(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/banque.html'
	return render(request,template,context)

def assurance(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/assurance.html'
	return render(request,template,context)

def energie(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/energie.html'
	return render(request,template,context)

def secteur_public(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/secteur_public.html'
	return render(request,template,context)

def telecommunications(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/telecommunications.html'
	return render(request,template,context)

def transport_et_logistique(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/transport_et_logistique.html'
	return render(request,template,context)

def a_propos(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()
	chiffre = Bdd_chiffre.objects.all()
	chiffre_en = Bdd_chiffre_anglais.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'a_propos.html'
	return render(request,template,context)


def nous_rejoindre(request):
	evenement = Bdd_evenement.objects.all().reverse()[0]
	reseaux = Bdd_reseaux.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	if request.method == "POST":
		Nom = request.POST.get('nom')
		subject = Nom +" - Oxade Consulting Nous rejoindre"
		emailFrom = request.POST.get('mail')
		emailTo =[settings.EMAIL_HOST_USER]

		# with open(setting.BASE_DIR + "template/newsletters/sign_up_email.txt") as f:
		#  	sign_up_message = f.read()
		message = EmailMultiAlternatives(subject=subject, from_email=emailFrom, to=emailTo)
		html_template = get_template("templates_emails/email_nous_rejoindre.html").render()
		message.attach_alternative(html_template, "text/html")
		message.send()




		# image = request.FILES['cv']
		# print(image.name)
		# print(image.size)

	# if request.POST.get('envoyer'):

		# Nom =  request.POST.get('nom')
		# subject = Nom +" - Oxade Consulting Nous rejoindre"
		# cv_name = request.POST.get('cv')


		# Fromadd = request.POST.get('mail')
		# Toadd = [settings.EMAIL_HOST_USER]    ##  Spécification des destinataires
		# message = MIMEMultipart()    ## Création de l'objet "message"
		# message['From'] = Fromadd    ## Spécification de l'expéditeur
		# message['To'] = Toadd    ## Attache du destinataire à l'objet "message"
		# message['Subject'] = subject    ## Spécification de l'objet de votre mail
		# msg = "VOTRE MESSAGE"    ## Message à envoyer
		# message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))    ## Attache du message à l'objet "message", et encodage en UTF-8

		# nom_fichier = request.POST.get('cv')    ## Spécification du nom de la pièce jointe
		# piece = open('%s' %(nom_fichier), "rb")    ## Ouverture du fichier
		# part = MIMEBase('application', 'octet-stream')    ## Encodage de la pièce jointe en Base64
		# part.set_payload((piece).read())
		# encoders.encode_base64(part)
		# part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
		# msg.attach(part)    ## Attache de la pièce jointe à l'objet "message" 

		# serveur = smtplib.SMTP('smtp.gmail.com', 587)    ## Connexion au serveur sortant (en précisant son nom et son port)
		# serveur.starttls()    ## Spécification de la sécurisation
		# serveur.login(Fromadd, "VOTRE MOT DE PASSE")    ## Authentification
		# texte= message.as_string().encode('utf-8')    ## Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
		# serveur.sendmail(Fromadd, Toadd, texte)    ## Envoi du mail
		# serveur.quit()    ## Déconnexion du serveur

		# Nom =  request.POST.get('nom')
		# tel = request.POST.get('tel')
		# mail = request.POST.get('email')

		# subject = Nom +" - Oxade Consulting Nous rejoindre"
		# emailFrom = request.POST.get('mail')
		# emailTo =[settings.EMAIL_HOST_USER]

		# cv = request.FILES['cv']
		# cv_name = cv.name
		# cv_contenu = cv.chunks()

		# lettre = request.FILES['lettre']
		# lettre_name = lettre.name
		# lettre_contenu = lettre.chunks()
		
		# message ='Nom : %s\nTéléphone : %s\nMail : %s\n' %(Nom, tel, mail)
		
 
		# msg = EmailMessage(subject,message, emailFrom, emailTo, attachments=((cv_name, cv_contenu, 'image/png'),(lettre_name, lettre_contenu,'image/png')))
		# msg.send(fail_silently=False)
		
		# send_mail(subject, message, emailFrom, emailTo, fail_silently=True)  




	context = locals()
	template = 'nous_rejoindre.html'
	return render(request,template,context)


