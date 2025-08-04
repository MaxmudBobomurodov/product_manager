from django.db import models
from django.utils.translation import gettext_lazy as _
class Products(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("name"))
    quantity = models.CharField(max_length=100, verbose_name=_("quantity"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))
