from django.db import models

# Create your models here.
class WishList(models.Model):
    name = models.TextField(max_length=300)