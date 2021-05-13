from django.contrib import admin
import mptt
from django.contrib.admin import models
from django.db import models
from mptt.fields import TreeForeignKey, TreeManyToManyField
from mptt.admin import DraggableMPTTAdmin
from django.contrib.admin.options import ModelAdmin
from mptt.admin import MPTTModelAdmin

from django.contrib.auth.models import Group
from .models import Category, Letter
from accounts.models import Profil

class UserProfileAdmin(admin.ModelAdmin):
    #list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)

        #queryset = queryset.order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'Info'

# treeforeign key
# add a parent foreign key

# filterspecs




admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Letter, order_insertion_by=['litera'])
TreeForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True).contribute_to_class(Group, 'parent')

mptt.register(Group, order_insertion_by=['name'])
