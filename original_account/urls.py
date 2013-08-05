from django.conf.urls import url,patterns,include 
from original_account.views import register,Login,sent

urlpatterns = patterns('',
	url(r'^register/$',register),
	url(r'^login/$',Login),
	url(r'^mail/$',sent),
	#url(r'^editprofile/$',edit_profile),
)
