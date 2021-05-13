from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.models import User
from listy.models import Category, Letter
from accounts.models import Profil
#paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator





class lista_miast(ListView):
    context_object_name = "models"
    template_name = 'genres.html'
    queryset = Category.objects.all()
    def paginator (request):
        paginator = Paginator(queryset, 10)
        page_number = request.GET.get("page", 1)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
    def get_context_data(self,**kwargs):
        context= super(lista_miast, self).get_context_data(**kwargs)
        context['letter']=Letter.objects.all
        context['bycategory'] = Category.objects.filter(parent=None)
        context['category'] = self.queryset
        context['a'] = Category.objects.filter(title__istartswith='a', parent=None)
        context['b'] = Category.objects.filter(title__istartswith='b', parent=None)
        context['c'] = Category.objects.filter(title__istartswith='c', parent=None)
        return context





def kategoria(request, id):
    context = {}

    category = Category.objects.filter(id=id)
    category_children = Category.objects.filter(parent__in=category)
    profil = Profil.objects.filter(kategoria__in=category)

    paginator = Paginator(category_children, 10)
    page_number = request.GET.get("page", 1)
    try:
        page= paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context =  {
        'cat' : category,
        'category_children' : category_children,
        'profil': profil

    }

    return render(request, "listaprofili.html", context)

def subkategoria(request,id):
    category = Category.objects.filter(id=id)
    category_children = Category.objects.filter(parent__in=category)
    profil = Profil.objects.filter(kategoria__in=category)
    paginator = Paginator(category_children, 10)
    page_number = request.GET.get("page", 1)
    try:
        page= paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context = {
        'cat': category,
        'category_children': category_children,
        'profil': profil

    }
    return render(request, "listaprofili.html", context)
def profil_view (request, id):
    profil = get_object_or_404(Profil, pk=id)

    args = {
        'profil' : profil,
    }
    return render(request, 'profil_widok.html', args)

