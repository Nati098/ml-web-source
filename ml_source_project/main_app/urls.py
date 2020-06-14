from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from main_app import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^help/$', views.help_, name='help'),
    re_path(r'^articles/(?P<type_>\w+)$', views.articles, name='articles'),
    re_path(r'^articles/(?P<type_>\w+)&(?P<article_id>\d+)/$', views.article_details, name='article_details'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.user_login, name='login'),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="auth/logged_out.html"), name='logout'),

    # change password urls
    # url(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name="password_change_form.html"),  name='password_change'),
    # url(r'^password-change/done/$', auth_views.PasswordChangeDoneView(template_name='password_change_done.html'), name='password_change_done'),

    # restore password urls
    # url(r'^password-reset/$', auth_views.PasswordResetView(template_name="password_reset_form.html"), name='password_reset'),
    # url(r'^password-reset/done/$', auth_views.PasswordResetDoneView(template_name="password_reset_done.html"), name='password_reset_done'),
    # re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    # url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView(template_name="password_reset_complete.html"), name='password_reset_complete'),
]
