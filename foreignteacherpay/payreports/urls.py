from django.conf.urls import url, patterns
from payreports import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),

                       )