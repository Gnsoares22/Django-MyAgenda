from django.db import models
from django.contrib.auth.models import User

# Create your models here. RESPONSÁVEL PELA CRIAÇÃO DAS TABELAS


class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título do Evento')
    descricao = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=100, verbose_name='Local do Evento')
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'  # nome personalizado para tabela

    def __str__(self):
        return self.titulo

    def get_data_evento(self): # self = this
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')