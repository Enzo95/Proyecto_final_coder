from django.db import models

# Create your models here.
class Receta(models.Model):

    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=500)
    procedimiento = models.CharField(max_length=5000)

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo}"