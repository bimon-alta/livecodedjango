from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.IntegerField(default=0)
    img_url = models.CharField(max_length=255,default='')
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nama

class Description(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=255,default='')
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.description