from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
