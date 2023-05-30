from django.shortcuts import render

app_name="cliente"

def index(request):
    return render(request, "cliente/index_cliente.html")

def Formulario(request):
    return render(request,"cliente/tipo_de_instrumento.html")

