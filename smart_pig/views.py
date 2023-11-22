from django.shortcuts import render, redirect
from smart_pig.form import CadastroPorco
from smart_pig.models import Porco
# Create your views here.


def index(request):
    return render(request, 'smart_pig/index.html')


def porco(request):
    return render(request, 'smart_pig/porco.html')


def reg_porco(request):
    form = CadastroPorco

    if request.method == 'POST':

        form = CadastroPorco(request.POST)
        if form.is_valid():
            form.save()
            return redirect('porco')
    return render(request, 'smart_pig/form_reg.html', {'form': form})


def rel_porco(request):
    porco = Porco.objects.all()
    return render(request, 'smart_pig/rel_porco.html', {'porco': porco})
