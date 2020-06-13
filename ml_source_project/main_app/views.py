from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from main_app.forms import ArticleForm
from main_app.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def articles(request, type_):
    articles_ = None
    title_ = ''
    if type_ == 'article':
        articles_ = Article.objects.all()
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




