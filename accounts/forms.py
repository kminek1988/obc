from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#category
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap, helper
from mptt.forms import TreeNodeChoiceField
#moje
from listy.models import Category
from accounts.models import Profil
from mptt.forms import TreeNodeChoiceField
from  django.utils.safestring import  mark_safe



class RejestracjaForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',




        ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profil

        fields = [
            'imie',
            'nazwisko',
            'profilimg',
            'opis',
            'kategoria',
            'kod',
            'strona',
            'telefon',
            'profesja',
            'miasto',
            'port1',
            'port2',
            'port3',
            'port4',
            'port5',]


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [

        ]