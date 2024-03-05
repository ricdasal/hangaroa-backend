from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField()
    imagen = models.TextField()
    estado =  models.BooleanField()


