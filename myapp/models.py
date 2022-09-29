from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nombre)

class Tema(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.materia)