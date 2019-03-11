from django.db import models



# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Pf(models.Model):
    canal = models.CharField(max_length=50)
    codigotrs = models.CharField(max_length=50)
    date = models.CharField(max_length=50)


