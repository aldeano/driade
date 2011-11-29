from django.conf.urls.defaults import patterns, include, url
from calcs.views import *

urlpatterns = patterns('',
    url(r'^(?P<purpose>\w+)/$', phenology, name='fenologia'),
    #url(r'^heat/$', heat, name='heat'),
    #url(r'^evapo/$', evapo, name='evapo'),
    url(r'^new_calc/$', phenology, name='fenologia'),
    url(r'^$', home, name='home_calcs'),
)
