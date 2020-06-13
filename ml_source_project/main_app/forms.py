# from django import forms
# from django.utils.translation import ugettext_lazy as _
#
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from main_app.models import UserRole
#
#
# class CustomUserEditForm(UserChangeForm):
#     country = forms.CharField(required=True, label=_("Country"))
#     status = forms.ModelChoiceField(queryset=UserRole.objects, required=True, label=_("Role"))
#
#
# class CustomUserCreationForm(UserCreationForm):
#     country = forms.CharField(required=True, label=_("Country"))
#     status = forms.ModelChoiceField(queryset=UserRole.objects, required=True, label=_("Role"))
