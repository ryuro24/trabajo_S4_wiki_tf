from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=30)
    rol = models.ForeignKey(
        Rol, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email