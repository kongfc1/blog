from django.db import models

# Create your models here.

# # Create your models here.
class Menu(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=30,unique=True)
