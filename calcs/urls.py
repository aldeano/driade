from django.conf.urls.defaults import patterns, include, url
from calcs.views import *

urlpatterns = patterns('',
    url(r'^explanation/(?P<purpose>\w+)/$', ajax_expl),
    url(r'^(?P<purpose>\w+)/$', phenology, name='fenologia'),
)
