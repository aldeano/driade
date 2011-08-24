from django.conf.urls.defaults import patterns, include, url
from calcs.views import *

urlpatterns = patterns('',
    url(r'^chill/$', chill, name='chill'),
    url(r'^heat/$', home, name='heat'),
    url(r'^evapo/$', home, name='evapo'),
    url(r'^$', home, name='home_calcs'),
)
