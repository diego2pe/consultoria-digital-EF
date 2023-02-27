from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.from django.shortcuts import render
def consultora(request,*cadena,**cadenaI):
 
    return render(request,'pagina/consultoria.html')   