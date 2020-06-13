from django.conf.urls import url
from django.urls import path, re_path
from main_app import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^help/$', views.help_, name='help'),
    re_path(r'^articles/(?P<type_>\w+)$', views.articles, name='articles'),
    re_path(r'^articles/(?P<type_>\w+)&(?P<article_id>\d+)/$', views.article_details, name='article_details'),
]
