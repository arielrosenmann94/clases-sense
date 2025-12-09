from django.shortcuts import render

def calculo_iva(request):
    return render(request, 'ejemplos/calculo_iva.html')
