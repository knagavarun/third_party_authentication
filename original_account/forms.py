from django import forms
from original_account.models import UserProfile
from captcha.fields import ReCaptchaField
from mysite.settings import RECAPTCHA_PUBLIC_KEY,RECAPTCHA_PRIVATE_KEY
class SampleRegistrationForm(forms.ModelForm):
	class Meta:
		model = UserProfile
class RegistrationForm(SampleRegistrationForm):
	username   = forms.CharField(max_length=20)
	password   = forms.CharField(max_length=20,widget=forms.PasswordInput)	
	first_name = forms.CharField(max_length=20)
	last_name  = forms.CharField(max_length=20)
	email_id   = forms.EmailField(max_length=20)
	class Meta(SampleRegistrationForm.Meta):
		fields = ('username','password','email_id','first_name','last_name',\
				  'gender','age','mobilenumber',)
class LoginForm(forms.Form):
	captcha = ReCaptchaField(
			  public_key=RECAPTCHA_PUBLIC_KEY,
			  private_key=RECAPTCHA_PRIVATE_KEY,
			  attrs={'theme':'clean'}
			  )
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30,widget=forms.PasswordInput) 
#class sampleedituserform(forms.ModelForm):
#	class Meta:
#		model=UserProfile
#class edituserform(sampleedituserform):
#	class Meta(sampleedituserform.Meta):
#		fields = (\
#				  'mobilenumber') 

