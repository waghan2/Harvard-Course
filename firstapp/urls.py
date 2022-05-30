from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    #este exemplo abaixo a url é firstapp/mundo, o name não está sendo utilizado....
    path("mundo", views.mundo, name="brian"),
    path("teste", views.teste, name="david"),
    #Neste exemplo abaixo eu recebo uma str:name e apresendo na views.interacao.
    #path("<str:name>", views.interacao, name="greet"),
    path("home", views.home, name="home")
    #agora vamos definir o retorno de uma pagina html:
    
    
]
