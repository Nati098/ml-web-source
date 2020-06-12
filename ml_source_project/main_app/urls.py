from django.conf.urls import url
from django.urls import path, re_path
from main_app import views

urlpatterns = [
    re_path(r'^$', views.home, name='index'),
]