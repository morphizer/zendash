from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$', 'dashboard.views.index'),
        url(r'^getevents/$', 'dashboard.views.getevents'),
        url(r'^configuration/$', 'dashboard.views.configuration'),
        )
