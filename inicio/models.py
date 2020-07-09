from django.db import models
import json


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=True)


class Facturas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()


class ChatModel(models.Model):
    usuario = models.CharField(max_length=100, null=True)
    texto = models.CharField(max_length=1000)
    fecha = models.DateTimeField(null=True, auto_now=True)



    def intencion(self):
        if self.texto:
             j = json.loads(self.texto)["intent"]
             return (j)
        return ""

    def entidades(self):
        if self.texto:
             j = json.loads(self.texto)["entities"]
             return (j)
        return ""

    class Meta:
        ordering = ('-fecha', )