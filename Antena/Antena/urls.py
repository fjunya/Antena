from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Antena.views.home', name='home'),
    url(r'^antena/', include('AntenaApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

