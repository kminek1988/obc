"""obc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from obc import settings
#home
from home.views import regulamin, rodo, polityka, Home
from accounts.views import profil, Edycja, rejestracja, activate
from listy.views import lista_miast, profil_view, subkategoria, kategoria
from contact.views import add_or_change_contact


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    #home
    path('', Home.as_view(), name="homepage"),
    path('regulamin/', regulamin, name='regulamin'),
    path('polityka-prywatnosci/', polityka, name='polityka'),
    path('rodo/', rodo, name='rodo'),
    #szukajka
    url(r'^search/', include('haystack.urls')),
    # auth + reset hasła
    path('accounts/', include('django.contrib.auth.urls')),
    path('rejestracja/', rejestracja, name="rejestracja"),
    path('edycja/', Edycja, name='edycja'),
    path('profil/', profil, name="profil"),
    # aktywacja konta
    path('verification/', include('verify_email.urls')),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    #listy
    # listy
    path('genres/', lista_miast, name="lista_miast"),
    path('kategoria/<int:id>/', kategoria, name='kategoria'),
    path('kategoria/<int:id>/', subkategoria, name='subkategoria'),
    path('profil_view/<int:id>', profil_view, name='profil_view'),
    path('miasta/', lista_miast.as_view(), name="miasta"),  # pierwsza strona miast
    path('<int:id>', profil_view, name='profil_view'),
    #postman_menu
    path('messages/', include('postman.urls'), name='postman'),
    #contact
    path('nowy/', add_or_change_contact, name="nowy"),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
