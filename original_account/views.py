from django.http import *
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from original_account.models import UserProfile
from original_account.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from original_account.models import SUserProfile
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			#print('yes')		
			data = form.cleaned_data			
			newuser = User(username = data['username'],email=data['email_id'],first_name=data['first_name'],last_name=data['last_name'])
			newuser.set_password(data['password']) 
			newuser.save()
			userprofile = UserProfile(
			user = newuser,
			#name = data['name'],			
			gender = data['gender'],
			age = data['age'],
			mobilenumber = data['mobilenumber'],
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
			user=authenticate(username=username,password=password)
			if user is not None:
				#if user.is_active:
				login(request,user)
				return HttpResponse("thankyou")
		#		else:
		#			error_message = "your account has been disabled"
		#			return render_to_response('original_account/login.html',locals(),context_instance=RequestContext(request))			
			else:
				print('nono')					
				error_message = "your username and password didn't match"
				form=LoginForm()
				return render_to_response('original_account/login.html',locals(),context_instance=RequestContext(request))	
	else:
		form = LoginForm()
	return render_to_response('original_account/login.html',locals(),context_instance=RequestContext(request))
def Logout(request):
	logout(request)
	return render_to_response('original_account/logout.html',context_instance=RequestContext(request))
def home(request):	
	try:
		old_user=SUserProfile.objects.get(email_id='knagavarun@gmail.com')
		username=old_user.provider
	except:
		username=None
	return render_to_response('original_account/home.html',locals(),context_instance=RequestContext(request))
def sent(request):
	connection = EmailBackend	
	print('p')
	send_mail('test mail', 'sending mail from shaastra id', 'shaastra@shaastra.org', ['knagavarun@gmail.com'], fail_silently=False)
	print('q')	
	return HttpResponse('thank you')
			
