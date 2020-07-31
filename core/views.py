from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages


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
    # usuario = request.user pegar os dados referente ao usuário logado
    evento = Evento.objects.all()  # get(id=1) get = where consulta semelhante ao select
    # evento = Evento.objects.filter(usuario = usuario)
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


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def cadastrar_eventos(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data = request.POST.get('data-evento')
        local = request.POST.get('local-evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo = titulo, data_evento = data, local = local, descricao = descricao, 
        usuario = usuario)
        return redirect('/')
    return redirect('/')
