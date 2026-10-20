from django.shortcuts import render

# Create your views here.

def perfil(request):
    return render(request, 'perfil.html')

def completar_cadastro(request):
    return render(request, 'completar_cadastro.html')

def esqueci_senha(request):
    return render(request, 'esqueci-senha.html')