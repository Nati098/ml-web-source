from django import forms
from main_app.models import *


class ArticleForm(forms.ModelForm):
    article = forms.ModelChoiceField(queryset=Article.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Article
        # список имен модели, которые будут присутствовать в форме
        fields = ('title', 'content', 'date')
