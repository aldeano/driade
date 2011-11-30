from django.conf.urls.defaults import patterns, include, url
from calcs.views import *

urlpatterns = patterns('',
    url(r'^(?P<purpose>\w+)/$', phenology, name='fenologia'),

)
