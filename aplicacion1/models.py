from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=100, null=False)
    edad=models.IntegerField()
    email=models.EmailField()