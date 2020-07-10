import requests
from django.db import models
import json

class Frases(models.Model):
    frase =  models.CharField(max_length=1000)
    entidades = models.CharField(max_length=1000)
    resultado = models.CharField(max_length=1000, null=True)

    @staticmethod
    def procesar():
        for frase in Frases.objects.all():
            json_data = {
                "text": frase.frase,
                "message_id": "11",
            }
            datos = requests.post('http://localhost:5005/model/parse/', json=json_data)
            frase.resultado = datos.text
            frase.save()

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