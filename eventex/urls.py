# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('eventex.core.urls', namespace='core')),
)
