from django.contrib import admin
from .models import Profil
# Register your models here.
class ProfilAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profil, ProfilAdmin)
