from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','local','data_evento','data_criacao')
    list_filter = ('titulo',)

admin.site.register(Evento, EventoAdmin) #registrando a models aqui 
