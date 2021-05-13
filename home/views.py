from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from accounts.models import Profil
from django.db.models import Q
import re
from home.forms import szukajkaForm

# Create your views here.
'''
Widom homeview
'''
class Home(TemplateView):
   template_name = 'home.html'

def szukajka(request):
   template_name = 'search.html'
   context = {
      'form': szukajkaForm
   }
   return render(request, 'search/search.html', context)

def rodo(request):
   return render(request, "rodo.html")

def polityka(request):
   return render(request, "polityka.html")

def regulamin(request):
   return render(request, "regulamin.html")