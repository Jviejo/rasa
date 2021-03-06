from django.urls import reverse
from django.views.generic import CreateView
import requests
from inicio.models import ChatModel
import json


class ProcesoChat(CreateView):
    template_name = "chat.html"
    model = ChatModel
    fields = ["texto"]

    def conversacion(self):
        return ChatModel.objects.all()

    def get_success_url(self):
        return reverse('chat')

    def form_valid(self, form):
        data = form.cleaned_data
        json_data = {
            "text": data['texto'],
            "message_id": "12",
        }


        datos = requests.post('http://localhost:5005/model/parse/', json=json_data)
        print(datos.text)
        #
        #
        #
        # datos1 = requests.post('http://localhost:5005/conversations/default/messages', json={
        #     "text": data['texto'],
        #     "sender": "default"
        # }
        #                        )
        # print(datos1)
        #

        if data['texto'] == 'limpiar':
            ChatModel.objects.all().delete()
        self.object = form.save(commit=False)
        self.object.usuario = 'bot'
        self.object.texto = datos.text
        self.object.save()

        if data['texto'] == 'domain':
            s = requests.Session()
            s.headers.update({"accept": 'application/json'})
            datos = s.get('http://localhost:5005/domain')
            print('respuesta')
            print(datos.text)
        if data['texto'] == 'status':
            s = requests.Session()
            s.headers.update({"accept": 'application/json'})
            datos = s.get('http://localhost:5005/status')
            print('respuesta')
            print(datos.text)

        return super().form_valid(form)
