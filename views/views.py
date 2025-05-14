from django.shortcuts import render, redirect
from django.utils import timezone
from models import ConsultaCNPJ
from forms import ConsultaCNPJform
from scraper import consultarProtesto

def listar_cnpjs(request):
    cnpjs = ConsultaCNPJ.objects.all().order_by('-id')
    return render(request, 'consultas/listar.html', {'cnpjs': cnpjs})

def adicionar_cnpjs(request):
    if request.method == 'POST':
        form = ConsultaCNPJform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cnpjs')
    else:
        form = ConsultaCNPJform()
    return render(request, 'consultas/adicionar.html', {'form': form})

def consultar_todos(request):
    pendentes = ConsultaCNPJ.objects.filter(status='pendente')
    for cnpj_obj in pendentes:
        resultado = consultarProtesto(cnpj_obj.cnpj)
        cnpj_obj.resultado = resultado
        cnpj_obj.status = 'consultado'
        cnpj_obj.consultado_data = timezone.now()
        cnpj_obj.save()
    return redirect ('listar_cnpjs')