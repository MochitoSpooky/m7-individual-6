from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Terminada', 'Terminada'),
    ]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}|{self.estado}" 
