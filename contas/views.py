from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
# Create your views here.


def horario(request):
    hora = datetime.now()
    html = f'<head><body> A hora é {hora} </body></head>'
    return HttpResponse(html)


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form': form})