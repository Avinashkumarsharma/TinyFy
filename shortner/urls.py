'''
Created on Jul 9, 2012

@author: Avi
'''
from django.conf.urls.defaults import patterns
from shortner import views
urlpatterns=patterns('',(r'^$',views.tiny),
                      (r'^show/$',views.showurl),
                      (r'^([mn6j2c4rv8bpygw95z7hsdaetxuk3fq]{5})/$', views.redirect_to),
                      )
