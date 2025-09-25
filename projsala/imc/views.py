from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Bem vindo(a) à aplicação IMC</h1>")

def nome(request):
    return HttpResponse("<h1>Wellington Coutinho</h1>")

def tabuada(request):
    html = '<table border="1"><tr><td><b>Tabuada de Sete</b></td></tr>'
    for i in range(1, 11):
        html += f"<tr><td>7 x {i} = {7 * i}</td></tr>"
    html += "</table>"

    return HttpResponse(html)
