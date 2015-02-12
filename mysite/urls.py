from django.conf.urls import patterns, include, url
from django.contrib import admin

from polls import views

from django.http import HttpResponseRedirect, HttpResponse

urlpatterns = patterns('',
    (r'^$', lambda r: HttpResponseRedirect('/admin')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
