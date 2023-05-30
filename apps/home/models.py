from django.db import models

class Cliente(models.Model):
    
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()

class Comprador(models.Model):
    
    campo3 = models.CharField(max_length=100)
    campo4 = models.BooleanField()

class Producto(models.Model):
    
    campo5 = models.CharField(max_length=100)
    campo6 = models.DateField()

