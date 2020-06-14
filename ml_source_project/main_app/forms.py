from django import forms
from django.contrib.auth.models import User
from main_app.models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

# class ArticleForm(forms.ModelForm):
#     article = forms.ModelChoiceField(queryset=Article.objects.all(), widget=forms.HiddenInput)
#
#     class Meta:
#         model = Article
#         # список имен модели, которые будут присутствовать в форме
#         fields = ('title', 'content', 'date')
