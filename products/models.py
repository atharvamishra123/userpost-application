from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20, null=False)
    weight = models.FloatField(max_length=20, null=False)
    price = models.FloatField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
