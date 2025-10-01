from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
def index(request):
  return render(request, 'index.html')
def calcular_imc(request):
    altura = float(request.GET.get('altura'))
    peso = float(request.GET.get('peso'))
    imc= peso/(altura*altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
    contexto= {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto)

