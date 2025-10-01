from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("calcular/", views.calcular_imc, name="calcular_imc" ),
]