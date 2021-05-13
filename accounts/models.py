from django.contrib.auth.models import User, AbstractUser
from django.db import models

from mptt.fields import TreeManyToManyField
from django.urls import reverse
from listy.models import Category
from django.conf import settings
from django.contrib.auth import get_user_model


#

class ProfilManager(models.Manager):
    pass


# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    imie = models.CharField(max_length=50, null=True, blank=True, default="")
    nazwisko = models.CharField(max_length=50, null=True, blank=True, default="")
    profilimg = models.ImageField(upload_to='media/profiles/', blank=True, null=True, default='media/1.jpg')
    opis = models.TextField(blank=True)
    kategoria= models.ForeignKey(Category, verbose_name="Kategoria", null=True, blank=True, on_delete=models.DO_NOTHING)
    kod = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    strona =  models.CharField(max_length=255, null=True, blank=True, default="np www.mojadomena.pl")
    telefon = models.CharField(max_length=50, null=True, blank=True, default="")
    profesja = models.CharField(max_length=50, null=True, blank=True, default="")
    miasto = models.CharField(max_length=50, null=True, blank=True, default="")
    port1 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/1.jpg', verbose_name="galeria zdjęcie nr 1")
    port2 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/1.jpg', verbose_name="galeria zdjęcie nr 2")
    port3 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/1.jpg', verbose_name="galeria zdjęcie nr 3")
    port4 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/1.jpg', verbose_name="galeria zdjęcie nr 4")
    port5 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/1.jpg', verbose_name="galeria zdjęcie nr 5")


    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"
    def __str__(self):
        return f'{self.user.username}'
    def get_absolute_url(self):
        return reverse('profil_view', args=[str(self.id)])


