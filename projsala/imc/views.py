from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .services import IMCServices

def index(request):
  return render(request, 'index.html')

def calcular_imc(request):
    altura = float(request.GET.get('altura'))
    peso = float(request.GET.get('peso'))
    imc, classificacao = IMCServices.calcular(peso, altura)

    contexto= {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto)

