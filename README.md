# Django-MyAgenda
Sistema de gerenciamento de agendas e tarefas com notificações de lembretes. 
<br> <br>


<h1> Pré-Requesitos </h1>

IDE Utilizada: VSCODE

Versão Python: 3.8.2

Versão do Django-Admin: 3.0.8

pip freeze: lista todas as ferramentas instaladas do python

pip xx: gerenciador de pacotes do python 

<br>

<h2> Ambiente Virtual </h2>

Para criar um ambiente virtual: virtualenv nome_da_virtualenv

Iniciar ambiente virtual: cd nome_da_virtualenv/Scripts/activate ou .\activate

<br>


<h2> Instalação Django </h2>

pip install django: instala o framework web django

 Iniciar um projeto : django-admin startproject nome_projeto

 Rodar o projeto: python manage.py startapp ou python manage.py runserver

 Criar uma app: django-admin startapp nome_app pro

<br>

<h2> Criar Tabelas  </h2> 

Criar tabelas: python manage.py migrate

Criar um super usuário para logar no django-admin: python manage.py createsuperuser --username admin

Fazer uma migração de uma nova classe: python manage.py makemigrations core <-- nome do app (core)

Mandar essa migração para o banco: python manage.py sqlmigrate core 0001 <-- numero da migração gerada

Confirmar a migração: python manage.py migrate core 0001 <-- numero da migração

<br>

<b> DÚVIDAS DOS COMANDOS DO DJANGO: django-admin --help </b>

<br>

Feito com muito amor :heart: e carinho por Gabriel Nascimento Soares.

<br>

<strong> "EU SINCERAMENTE ESTOU AMANDO PYTHON  :snake:" </strong> (Gabriel N. Soares, 2020)
