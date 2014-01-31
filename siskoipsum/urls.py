from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'quote.views.home', name='home'),
    url(r'^sisko/(?P<paragraphs>[0-9]+)/(?P<length>[a-z]+)/$', 'quote.views.ajax_response', name='ajax_response'),

    url(r'^admin/', include(admin.site.urls)),
)
