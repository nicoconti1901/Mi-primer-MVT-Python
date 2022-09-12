from django.db import models



class Familiar(models.Model):
    nombre = models.CharField(max_length=60)
    clase = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaNacimiento = models.CharField(max_length=60)
