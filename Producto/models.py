from django.db import models

# Create your models here.

class Productos(models.Model):
    codigo_producto = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    nombre_producto = models.CharField(max_length= 20)
    categoria = models.CharField(max_length=20)
    stock_min = models.IntegerField()
    stock_max = models.IntegerField()
    unidad = models.CharField(max_length= 20)
    cant_stock = models.IntegerField()
    Estado = models.CharField(max_length= 20)
    observaciones = models.CharField(max_length=75)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.fecha_ingreso, self.id)