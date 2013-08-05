from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
	user         = models.OneToOneField(User)
	gender       = models.CharField(max_length = 1, choices = [('M','Male'),('F','Female')])
	age          = models.IntegerField()
	mobilenumber = models.CharField(max_length=20,blank=True)
class SUserProfile(models.Model):
	email_id   = models.EmailField(max_length=30)
	susername  = models.CharField(max_length=30,blank=True)	
	first_name = models.CharField(max_length=30,blank=True)
	last_name  = models.CharField(max_length=30,blank=True)
	provider   = models.CharField(max_length=30,blank=True)
	def __unicode__(self):
		return self.email_id
