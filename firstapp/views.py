from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse("Oi mãe\n primeio teste com django!")

def mundo(request):
    return HttpResponse("Olá, mundo!")

def teste(request):
    return HttpResponse("olá meus queridos, teste de url!")

#def interacao(request, name):
 #   return HttpResponse(f"Você digitou: {name}!")

#vamos definir uma função que devolva o html da home, uma documento html inteiro!
def home(request):
    return render(request, 'firstapp/index.html')
# aqui finalizamos os exemplos deste primeiro aplicativo.
#Vamos iniciar um novo aplicativo utilizando o django com interações com o python.
#na aula de harvard ele dá o exemplo do newyeasr.
# PS: Comando para criar um novo app é python manage.py startapp nome_do_app