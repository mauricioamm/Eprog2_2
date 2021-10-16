from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.db import connection
from random import randint
from .models import dictclass
from .forms import DictForm

def listagem(request):
    data = {}
    data['lista']= dictclass.objetos.all()
    return render(request, 'dictapp/listagem.html', data)

def criar(request):
    data= {}
    form = DictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form']= form
    #return render(request, 'dictapp/form2.html', data)
    return render (request, 'dictapp/principal_vazio.html', data)

def update(request, pk):
    data={}
    lista = dictclass.objetos.get(pk=pk)
    form= DictForm(request.POST or None, instance= lista)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['lista']= lista
    return render(request, 'dictapp/principal.html', data)

def delete(request, pk):
    lista = dictclass.objetos.get(pk=pk)
    lista.delete()
    return redirect('url_listagem')

def principal_hidden(request, pk):
    data= {}
    objetinho = dictclass.objetos.get(pk=pk)
    form= DictForm(request.POST or None, instance= objetinho)
    data['form'] = form
    data['objetinho']= objetinho
    if request.POST.get('Resposta'):
        return redirect('url_principal', pk)
    data['form'] = form
    data['objetinho']= objetinho
    return render(request, 'dictapp/principal_hidden.html', data)

def principal(request, pk):
    data= {}
    objetinho = dictclass.objetos.get(pk=pk)
    form= DictForm(request.POST or None, instance= objetinho)

    if request.POST.get('Listagem'):
        return redirect('url_listagem')

    if request.POST.get('Novo'):
        return redirect('url_criar')

    if request.POST.get('Salvar'):
       data = {}
       objetinho = dictclass.objetos.get(pk=pk)
       form = DictForm(request.POST or None, instance=objetinho)
       if form.is_valid():
        form.save()
          # aqui o form é recarregado, mas continua na mesma página
        data['form'] = form
        data['objetinho'] = objetinho
        return render(request, 'dictapp/principal.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_listagem')

    if request.POST.get('primeiro'):
        #objetinho = dictclass.objetos.get(pk=1)
        #print(objetinho)
        n= 1
        return redirect('url_principal', pk=n)

    if request.POST.get('proximo'):
        campo = 'id'
        obj_ultimo = dictclass.objetos.last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = dictclass.objetos.get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        #valor_campo = getattr(obj_atual, campo)
        n= valor_campo + 1
        if n > total:
            n= 1
        return redirect('url_principal', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = dictclass.objetos.get(pk=pk)
        valor_campo = getattr(obj, campo)
        n= valor_campo - 1
        if n== 0:
            n= 1
        return redirect('url_principal', pk=n)

    if request.POST.get('Sortear'):
        campo = 'id'
        obj = dictclass.objetos.last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        #n_ordem = n_rand
        return redirect('url_principal_hidden', pk= n_rand)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = dictclass.objetos.last()
        valor_campo = getattr(obj, campo)
        n= valor_campo
        return redirect('url_principal', pk=n)

    data['form'] = form
    data['objetinho']= objetinho
    return render(request, 'dictapp/principal.html', data)

