from django.conf.urls import url,patterns,include 
from original_account.views import register,Login

urlpatterns = patterns('',
	url(r'^register/$',register),
	url(r'^login/$',Login),
	#url(r'^editprofile/$',edit_profile),
)
