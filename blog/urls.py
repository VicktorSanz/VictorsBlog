from django.conf.urls import include, url
from . import views



urlpatterns = [

        url(r'^$', views.post_list , name='index'),
        url(r'^perfil.html$', views.perfil,name='perfil'),
        url(r'^about.html$', views.about,name='about'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    ]