# Harvard-Course

## Seja bem vindo

Este é meu "caderno de anotações" do curso cs50's de Harvard.
Não é uma tradução do curso. São as implementações em Django, exemplos de documento HTML e exercicios.
Os exercicios eu modifiquei um pouco, para tentar entender e utilizar as ferramentas modificando-as de acordo com a minha vontade.

Sinta-se a vontade para dar uma olha.
As pastas não estão super organizadas, mas adicionei varios comentários nas funções.
Se vc é BR e também quer fazer este curso, entre no EDX.com o curso é gratuito sem certificado.

### Comandos mais utilizados

Instalando Django -> pip3 install Django (aqui pode ser pip3 ou pip... Primeiro tenho o python instalado na maquina, talvez seja necessário escolher a versão correta do python)

Iniciar o servidor -> python manage.py runserver
Criar um projeto em django -> django-admin startproject NOME_DO_PROJETO (sem espaço)

## Tópicos abordados até agora

### HTML E CSS

### INSTALANDO DJANGO, FRAMEWORK

Esse django framework é "tipo" uma biblioteca que cria varias pastas com varios arquivos nos quais vc pode trabalhar, estruturando aplicações com interações
de html, python e javascript.

## Onde estamos

## Exemplos html-> ok

Alguns exemplos muito basicos de um documento HTML.

## Aula 1. Entendendo a linguagem de marcação

Introdução a html e css.

## Exemplos Django, primeior app ->  ok

Instalando Django e conhecendo o Framework.

## Aula 2

Entendendo o Framework Django.
Eu uso windowns e vs Code.
Foi um pouco diferente para instalar as bibliotecas e o prórpio python, no curso ele utiliza um mac, mas não é nada de outro mundo. O mais estranho foi instalar o python da forma correta, para instalar o django é um simples pip install...

## Django app com interações -> Construindo

Nesta aula aprendemos a utilizar o Django com algumas interações.

## Aula 3

Aqui começa a ficar legal, conseguimos fazer algumas interações mudando o HTML da pagina.
Step by step:

- 1 - Vamos iniciar um novo APP dentro do projeto comando = python manage.py startapp NOME_DO_APP
- 2 - Incluir o app em settings.py lá no projeto que criamos.
- 3 - Crie um arquivo urls.py no dentro do app.
Agora ao tentar rodar o app newyear nada vai acontecer, antes temos que criar alguns arquivos.
Para ficar tudo no padrão, temos que criar uma pasta templates e dentro desta pasta um arquivo index.html. OBS: Este é o padrão que ensinam, não precisa ter este nome nem precisa criar pastas dentro de pastas.
O arquivo index.html é um html  que já tem interações.
Tudo que fica dentro dos "{}" é um código que pode ser executado dentro do html.
Continuando...
- 4 - Dentro do views.py defina uma função para renderizar uma pagina html. Aqui eu usei exatamente o mesmo código utilizado no curso.

```def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
```
<<<<<<< HEAD

=======
>>>>>>> a7744739d852f46a991d42484f2ecedee7c432bb
Não esqueça de importar datetime (biblioteca com funções de data e hora)

Esta função irá retornar uma página html, que é justamente a pagina que criamos dentro da pasta templates/newyear.
