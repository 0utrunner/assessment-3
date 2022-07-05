from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name
