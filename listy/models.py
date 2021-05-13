from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.
class Letter(models.Model):
    title = models.CharField(verbose_name="litera", max_length=200)

    class Meta:

        verbose_name = "litera"
        verbose_name_plural = "litery"
    def __str__(self):
        return self.title

class Category(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children", verbose_name="miasto")
    title = models.CharField(verbose_name="nazwa", max_length=200)
    litera = models.ForeignKey(Letter, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ["tree_id", "lft"]
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"
    class MPTTMeta:
        order_inspiration_by = ["title"]

    def __str__(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
            ancestors = [i.title for i in ancestors]
        except:
            ancestors = [self.title]

        return ' > '.join(ancestors[:len(ancestors) + 1])