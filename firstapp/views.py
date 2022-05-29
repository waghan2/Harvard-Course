from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse("Oi mãe\n primeio teste com django!")

def brian(request):
    return HttpResponse("Olá, mundo!")

def david(request):
    return HttpResponse("olá meus queridos, teste de url!")
def greet(request, name):
    return HttpResponse(f"Você digitou: {name}!")