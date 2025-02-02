from django.db import models

class Persona(models.Model):
    rol = models.CharField(max_length=50)  # 'Estudiant' o 'Professor'
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField(unique=True)
    moduls = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.cognom1} ({self.rol})"
