from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.EmailTest, name='EmailTest'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]
