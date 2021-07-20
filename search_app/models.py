from django.db import models
from django.db.models.base import Model

# Create your models here.


class Index(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=200)
    #id = models.BigAutoField(primary_key=True)
    
