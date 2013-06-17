from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user          = models.OneToOneField(User)
	gender        = models.CharField(max_length=10,choices=[('M','Male'),('F','Female')])
	age           = models.IntegerField(max_length=3)
	mobilenumber  = models.IntegerField(max_length=10)
	def __unicode__(self):
		return self.user.first_name
