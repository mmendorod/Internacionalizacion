from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.utils.translation import ugettext as _

# Create your views here.
def register(request):





	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, "usuario ya existente")
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, "correo ya existente")
				return redirect('register')
			else:		
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				print('usuario creado')
				return redirect('login')
		else:
			messages.info(request, 'Las contraseñas no coinciden')
			print("Las contraseñas no coinciden..")
			return redirect('register')
		return redirect("/")

	else:



		return render(request, 'register.html')

def login(request):
	from django.utils import translation
	#user_language = 'es'
	#translation.activate(user_language)
	#request.session[translation.LANGUAGE_SESSION_KEY]= user_language
	if translation.LANGUAGE_SESSION_KEY in request.session:
		del request.session[translation.LANGUAGE_SESSION_KEY]


	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request, 'Datos Incorrectos')
			return redirect("login")	


	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect("/")		
