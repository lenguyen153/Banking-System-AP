from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=250)
    