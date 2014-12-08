from django.conf.urls import patterns, include, url
from payreports import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foreignteacherpay.views.index_view', name='index_view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^$', include('payreports.urls')),
    (r'^accounts/', include('allauth.urls')),
)
