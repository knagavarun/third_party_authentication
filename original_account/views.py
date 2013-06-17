from django.http import *
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import *
from django.contrib.auth.models import User
from original_account.models import UserProfile
from original_account.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			#print('yes')		
			data = form.cleaned_data			
			newuser = User(username = data['username'],email_id=data['email_id'],first_name=data['first_name'],last_name=data['last_name'])
			newuser.set_password(data['password']) 
			newuser.save()
			userprofile = UserProfile(
			user = newuser,
			#name = data['name'],			
			gender = data['gender'],
			age = data['age'],
#			email_id = data['email_id'],
			)
			userprofile.save()
			#print('no')
			form=LoginForm()			
			return render_to_response('original_account/login.html', locals(),context_instance = RequestContext(request))
	else:
		form = RegistrationForm()
	return render_to_response('original_account/register.html', locals(),context_instance = RequestContext(request))
def Login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			print('yo')		
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				#login(request,user)
				return HttpResponse("thankyou")
			else:
				print('nono')					
				error_message = "your username and password didn't match"
				form=LoginForm()
				return render_to_response('original_account/login.html',locals(),context_instance=RequestContext(request))	
	else:
		form = LoginForm()
	return render_to_response('original_account/login.html',locals(),context_instance=RequestContext(request))


			
