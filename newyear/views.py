import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1 # esta função retorna true se o mes atual for igual a jan, e dia =  1. Voce pode testear retornando true para ver se muda para yes no html.
    })
    
    