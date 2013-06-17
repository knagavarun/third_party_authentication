from django import forms
from original_account.models import UserProfile
class SampleRegistrationForm(forms.ModelForm):
	#name      = forms.CharField#(max_length=30)
	#email_id  = forms.EmailField()
	#gender    = forms.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
	#age       = forms.IntegerField#(max_length=2)
	#Username  = forms.CharField(max_length=20)
	#password  = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = UserProfile
#		fields = ('name','email_id','gender','age','username','password')
class RegistrationForm(SampleRegistrationForm):
	username   = forms.CharField(max_length=20)
	password   = forms.CharField(max_length=20,widget=forms.PasswordInput)	
	first_name = forms.CharField(max_length=20)
	last_name  = forms.CharField(max_length=20)
	email_id   = forms.EmailField(max_length=20)
	class Meta(SampleRegistrationForm.Meta):
		fields = ('username','password','email_id','first_name','last_name',\
				  'gender','age','mobilenumber')
class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30,widget=forms.PasswordInput) 
#class sampleedituserform(forms.ModelForm):
#	class Meta:
#		model=UserProfile
#class edituserform(sampleedituserform):
#	class Meta(sampleedituserform.Meta):
#		fields = (\
#				  'mobilenumber') 

