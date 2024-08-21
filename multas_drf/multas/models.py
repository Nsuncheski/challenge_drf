from django.db import models


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    dueño = models.ForeignKey(Persona.nombre, on_delete=models.CASCADE)

class Multa(models.Model):
    id = models.AutoField(primary_key=True)
    patente:Vehiculo = models.ForeignKey(Vehiculo.patente, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    comentarios = models.TextField()

    def __str__(self):
        return f"{self.patente.patente} - {self.comentarios}"
