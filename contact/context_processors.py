from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profil
from contact.forms import ContactForm

from contact.models import Contact


# from contact.forms import ContactForm

def contact(request):
    profil = User.objects.filter(username=request.user)
    contact = Contact.objects.filter(owner__in=profil)
    return {

        'contact': contact
    }

def add_or_change_contact(request):
    return {
        'form':ContactForm()
    }

