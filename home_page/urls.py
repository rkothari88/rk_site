from django.conf.urls import patterns, url
from home_page import views

urlpatterns = patterns('', 
                       url(r'^$', views.index, name='index'))
