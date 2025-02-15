from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    contraseña = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Hasheamos la contraseña antes de guardarla
        if not self.pk or "contraseña" in kwargs.get("update_fields", []):
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
