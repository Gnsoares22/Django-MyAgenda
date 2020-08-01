from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, timedelta
from django.http import JsonResponse

# Create your views here.

''' def localEvento(request, titulo_evento):
    try:
        consulta = Evento.objects.get(titulo=titulo_evento)
        return HttpResponse(consulta.local)
    except Exception as ex:
        return httpResponse(ex) '''


# para acessar a view é necessário que o usuario esteja logado
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user # pegar os dados referente ao usuário logado
    data_atual = datetime.now() - timedelta(hours= 1) #lista os eventos com até 1 hora de atraso
    evento = Evento.objects.filter(usuario = usuario, data_evento__gt = data_atual)  # get(id=1) get = where consulta semelhante ao select
    # gt para valores maiores que || lt para valores menores que 
    # evento = Evento.objects.all() pega todos os dados
    dados = {'eventos': evento}
    # Não esqueça de registrar o caminho do template no settings.py em DIRS[()]
    return render(request, 'agenda.html', dados)


def index(request):
    return redirect('/agenda/')


def login(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:  # se for uma requisição do tipo post
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            dj_login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou login Inválidos") #Mensagem de erro pesonalizada
            return redirect('/login/')
   #else:
     #   return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/login/')



#Editando eventos 
@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)



@login_required(login_url='/login/')
def cadastrar_eventos(request):
    if request.POST:
        id_evento_cadastrado = request.POST.get('id')
        titulo = request.POST.get('titulo')
        data = request.POST.get('data-evento')
        local = request.POST.get('local-evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        if id_evento_cadastrado:
            Evento.objects.filter(id = id_evento_cadastrado).update(titulo = titulo, data_evento = data, local = local, descricao = descricao, 
            usuario = usuario)
        else:
            Evento.objects.create(titulo = titulo, data_evento = data, local = local, descricao = descricao, 
            usuario = usuario)
            return redirect('/')
    return redirect('/')


# Deletando eventos
@login_required(login_url='/login/')
def deletarEvento(request,id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id = id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

# transformando a lista de eventos em um arquivo json para consumo API
@login_required(login_url='/login/')
def json_lista_eventos(request, id_usuario):
    usuario = User.objects.get(id = id_usuario)
    evento = Evento.objects.filter(usuario = usuario).values('id','titulo') 
    return JsonResponse(list(evento), safe=False)

