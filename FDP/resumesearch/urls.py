'''
Created on 26-Jul-2015

@author: Proventuz
'''
# from django.conf.urls import include, url
# from django.contrib import admin
# admin.autodiscover() 
# urlpatterns = [
#   url(r'^admin/', include(admin.site.urls)),
#    url(r'^resumesearch/', include('resumesearch.urls')),
# ]

from django.conf.urls import patterns, include, url
from resumesearch.views import results
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'resumesearch.views.home'),
    url(r'^search_resume/$', 'resumesearch.views.search_resume'),
    url(r'^search/$', 'resumesearch.views.results'),
    url(r'^JDInterface/$', 'resumesearch.views.JDInterface'),
    url(r'^ResumeInterface/$', 'resumesearch.views.ResumeInterface'),   
    url(r'^ResultsByProfile/$', 'resumesearch.views.ResultsByProfile'),
    url(r'^ResultsByJD/$', 'resumesearch.views.ResultsByJD'),
    url(r'^derivedInfo/(?P<resumeNo>\w+)/$', 'resumesearch.views.derivedInfo' ),
)
