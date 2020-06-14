from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import ml_source_project.settings as settings
from django.urls import reverse

from main_app.forms import *
from main_app.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def articles(request, type_):
    articles_ = None
    title_ = ''
    if type_ == 'article':
        articles_ = Article.objects.order_by('title').all()
        title_ = 'Article'
    elif type_ == 'demo':
        articles_ = WebDemo.objects.all()
        title_ = 'Demo'
    elif type_ == 'material':
        title_ = 'Material'
    return render(request, 'articles.html', {'page_title': title_, 'page_type': type_, 'articles': articles_})


def article_details(request, article_id, type_):
    article = None
    if type_ == 'article':
        article = get_object_or_404(Article, id=article_id)
    elif type_ == 'demo':
        article = get_object_or_404(WebDemo, id=article_id)
    elif type_ == 'material':
        article = get_object_or_404(WebDemo, id=article_id)
    return render(request, 'article_details.html', {'article': article})


# def demos(request):
#     demos = WebDemo.objects.all()
#     return render(request, 'articles.html', {'page_title': 'Demos', 'articles': demos})


# def study_materials(request, idx1=0, idx2=0):
#     return render(request, 'study_materials.html', {})


def help_(request):
    return render(request, 'help.html', {})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next',
                                                                settings.LOGIN_REDIRECT_URL))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'auth/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'user_form': user_form})
