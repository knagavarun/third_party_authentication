from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from allauth.account.views import *
from allauth.socialaccount.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
	url(r'^original/', include('original_account.urls')),
    url('^login/$', login, name='account_login'),
    url('^logout/$', logout, name='account_logout'),
    url('^login/cancelled/$', login_cancelled, name='socialaccount_login_cancelled'),
    url('^login/error/$', login_error, name='socialaccount_login_error'),
)
