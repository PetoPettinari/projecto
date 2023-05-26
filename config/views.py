from django.http import HttpResponse
from django.shortcuts import render

def Saludo(request):
    return HttpResponse('<h1>Hola Mundo<h1>') 

