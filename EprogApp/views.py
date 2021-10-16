from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
import datetime
import os
import csv
from django.contrib.auth.views import LogoutView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Count

from random import randint
from django.contrib.auth.decorators import login_required

from .models import EprogModel, CalculosModel, SessaoModel, ProcedimentoModel
from .forms import EprogForm, CalculosForm, SessaoForm, ProcedimentoForm, ImageForm

#def LogoutView(request):
#    logout(request)

def sessao_upload(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    #objetinho = EprogModel.objetos.get(pk=pk)
    form = EprogForm(request.POST or None, instance=objetinho)

    if request.POST.get('Voltar'):
        return redirect('url_sessao', pk=pk)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            instance = form.save()
            caminho = instance.image.name
            caminho_mesmo = instance.image.path
            print('o nome é: ', caminho)
            print('o nome é: ', caminho_mesmo)
            objetinho.OndeFigura1 = '/media/' + caminho
            objetinho.save()
            return render(request, 'EprogApp/Sessao_Upload.html', {'form': form, 'objetinho': objetinho,'img_obj': img_obj})
    else:
        form = ImageForm()

    context={
        'form': form,
        'objetinho': objetinho,
    }

    return render(request, 'EprogApp/Sessao_Upload.html', context)


def clonar_model(request):
    objeto_novo = EprogModel.objetos.get(pk=1)
    objeto_novo.pk = None
    objeto_novo.save()
    old_objeto = EprogModel.objetos.get(pk=1)

    #return redirect('url_listagem')
    return render(request, "EprogApp/clonar_model.html")

    # Pra clonar só um registro, no mesmo model
    #objeto_novo = EprogModel.objetos.get(pk=1)
    #objeto_novo.pk = None
    #objeto_novo.save()

    #quiz = Quiz.objects.get(pk=pkofquiziwanttocopy)
    #quiz.pk = None
    #quiz.save()
    #old_quiz = Quiz.objects.get(pk=pkofquiziwanttocopy)
    #quiz.question_set=old_quiz.question_set.all()

def Editar_EprogModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    #objetinho = EprogModel.objetos.get(pk=pk)
    form = EprogForm(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = EprogModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = EprogModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Participante = ''
        objeto_novo.Ordem = pk_next
        objeto_novo.Topico = ''
        objeto_novo.Textao = ''
        objeto_novo.SuaResposta = ''
        objeto_novo.OndeFigura1 = ''
        objeto_novo.OndeFigura1 = ''
        objeto_novo.OndeFigura2 = ''
        objeto_novo.DuvidaComent = ''
        objeto_novo.OndeFigura1 = ''
        objeto_novo.Acertou = ''
        objeto_novo.Jafoi = ''
        objeto_novo.Ativada = ''
        objeto_novo.Corretas = ''
        objeto_novo.Porcentagem = ''
        objeto_novo.Marcador1 = ''
        objeto_novo.Marcador2 = ''
        objeto_novo.Marcador3 = ''
        objeto_novo.Marcador4 = ''
        objeto_novo.Marcador5 = ''
        objeto_novo.save()
        return redirect('url_Editar_EprogModel', pk=pk_next)
        #return redirect('url_Editar_EprogModelNovo')

    if request.POST.get('Salvar'):
        data = {}
        objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
        form = EprogForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_EprogModel.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_EprogModel', pk=1)

    if request.POST.get('primeiro'):
        # objetinho = dictclass.objetos.get(pk=1)
        # print(objetinho)
        return redirect('url_Editar_EprogModel', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = EprogModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = EprogModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_EprogModel', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = EprogModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_EprogModel', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = EprogModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_EprogModel', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_EprogModel.html', context)

def Editar_CalculosModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = CalculosModel.objetos.using(banquinho).get(pk=pk)
    #objetinho = EprogModel.objetos.get(pk=pk)
    form = CalculosForm(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = CalculosModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = CalculosModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Ordem = pk_next
        objeto_novo.Porcentagem = ''
        objeto_novo.Corretas = ''
        objeto_novo.Incorretas = ''
        objeto_novo.save()
        return redirect('url_Editar_CalculosModel', pk=pk_next)

    if request.POST.get('Salvar'):
        data = {}
        objetinho = CalculosModel.objetos.using(banquinho).get(pk=pk)
        form = CalculosForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_CalculosModel.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_CalculosModel', pk=1)

    if request.POST.get('primeiro'):
        return redirect('url_Editar_CalculosModel', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = CalculosModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = CalculosModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_CalculosModel', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = CalculosModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_CalculosModel', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = EprogModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_CalculosModel', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_CalculosModel.html', context)

def Editar_ProcedimentoModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = ProcedimentoModel.objetos.using(banquinho).get(pk=pk)
    #objetinho = EprogModel.objetos.get(pk=pk)
    form = ProcedimentoForm(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = ProcedimentoModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = ProcedimentoModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Participante = ''
        objeto_novo.Banco = ''
        objeto_novo.NomeCompleto = ''
        objeto_novo.Idade = ''
        objeto_novo.Acesso = ''
        objeto_novo.Botao_avalia = ''
        objeto_novo.SessaoAtual = ''
        objeto_novo.save()
        return redirect('url_Editar_EProcedimentoModel', pk=pk_next)

    if request.POST.get('Salvar'):
        data = {}
        objetinho = ProcedimentoModel.objetos.using(banquinho).get(pk=pk)
        form = ProcedimentoForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_ProcedimentoModel.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_ProcedimentoModel', pk=1)

    if request.POST.get('primeiro'):
        return redirect('url_Editar_ProcedimentoModel', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = ProcedimentoModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = ProcedimentoModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_ProcedimentoModel', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = ProcedimentoModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_ProcedimentoModel', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = ProcedimentoModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_ProcedimentoModel', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_ProcedimentoModel.html', context)

def Editar_SessaoModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = SessaoModel.objetos.using(banquinho).get(pk=pk)
    #objetinho = EprogModel.objetos.get(pk=pk)
    form = SessaoForm(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = SessaoModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = SessaoModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Ordem = ''
        #objeto_novo.Ordem = pk_next
        objeto_novo.Participante = ''
        objeto_novo.Modulo = ''
        objeto_novo.Sessao = ''
        objeto_novo.Dia = ''
        objeto_novo.Horario = ''
        objeto_novo.Tentativa = ''
        objeto_novo.Topico = ''
        objeto_novo.DuvidaComent = ''
        objeto_novo.Acertou = ''
        objeto_novo.save()
        return redirect('url_Editar_SessaoModel', pk=pk_next)

    if request.POST.get('Salvar'):
        data = {}
        objetinho = SessaoModel.objetos.using(banquinho).get(pk=pk)
        form = SessaoForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_SessaoModel.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_SessaoModel', pk=1)

    if request.POST.get('primeiro'):
        return redirect('url_Editar_SessaoModel', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = SessaoModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = SessaoModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_SessaoModel', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = SessaoModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_SessaoModel', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = SessaoModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_SessaoModel', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_SessaoModel.html', context)

def criar_tabela(request):
    v_participante = ''
    v_procedimento = ''

    if request.POST.get('criartabela'):
        with connection.cursor() as cursor:
            v_participante = str(request.POST.get('nome_participante'))
            v_procedimento = str(request.POST.get('nome_procedimento'))
            cursor.execute("CREATE TABLE "+v_participante+" (ordem INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, telefone VARCHAR)")

        context= {
            'v_participante': v_participante,
            'v_procedimento': v_procedimento
        }
        return render(request, "EprogApp/criar_tabela.html", context)

    context = {
        'v_participante': v_participante,
        'v_procedimento': v_procedimento
    }
    return render(request, "EprogApp/criar_tabela.html", context)

@login_required
def teste_view(request):
        query_Eprog = EprogModel.objetos.all()
        query_Calculos = CalculosModel.objetos.all()
        objetinho2 = CalculosModel.objetos.get(pk=1)

        context = {
            "object_list_Eprog": query_Eprog,
            "object_list_Calculos": query_Calculos,
            "objetinho2": objetinho2
        }
        return render(request, "EprogApp/teste.html", context)

def teste2_view(request):
    objetinho2 = CalculosModel.objetos.get(pk=1)
    aumentado = objetinho2.Corretas
    mudou = "xxxx"

    if request.POST.get('correta'):
        objetinho_tcorretas = CalculosModel.objetos.get(pk=1)
        totalcorretas = objetinho_tcorretas.Corretas
        totalcorretas += 1
        mudou = totalcorretas
        objetinho_tcorretas.Corretas = totalcorretas
        objetinho_tcorretas.save()

        objetinho2 = CalculosModel.objetos.get(pk=1)
        context = {
            "objetinho2": objetinho2,
            "aumentado": aumentado,
            "mudou": mudou
        }
        return redirect('url_teste2_view')

    objetinho2 = CalculosModel.objetos.get(pk=1)
    context = {
            "objetinho2": objetinho2,
            "aumentado": aumentado,
            "mudou": mudou
        }
    return render(request, "EprogApp/teste2.html", context)

def teste_loop(request):
    user = request.user
    banquinho = str(user)

    if request.POST.get('Rodar_loop'):
        listax= EprogModel.objetos.using(banquinho).values_list('Ordem', 'Topico')
        for item in listax:
            print(item)

    return render(request, 'EprogApp/teste_loop.html')


def parabens_view(request):
    return render(request, "EprogApp/Parabens.html")

def Entrada(request):
    return render(request, "EprogApp/Entrada.html")

def Entrada_login(request):
    usuario = request.user
    if request.POST.get('Visitante'):
        #request.user = User.objects.get(username='visitante')
        usuario = User(username='visitante')
        #u = User.objects.get(username='visitante')
        #u.save()
    context= {
            "user": usuario
    }
    return render(request, "EprogApp/Entrada_login.html", context)

@login_required
def Entrada_Iniciar(request):
    user = request.user
    banquinho = str(user)
    #lista = EprogModel.objetos.using(banquinho).all()


    if request.POST.get('comecar_sessao'):
        user = request.user
        banquinho = str(user)

        # mudar sessao - inicio
        objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
        objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
        SessaoAntiga = objeto_procedimento.SessaoAtual
        n_SessaoAntiga = int(SessaoAntiga)
        n_SessaoAtual = n_SessaoAntiga + 1
        objeto_procedimento.SessaoAtual = str(n_SessaoAtual)
        objeto_procedimento.save()
        objetinho_sessao.Sessao = objeto_procedimento.SessaoAtual
        objetinho_sessao.save()
        # mudar sessao - fim

        campo = 'id'
        obj = EprogModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar', pk=n_rand)
    return render(request, "EprogApp/Entrada_iniciar.html")

@staff_member_required
def Entrada_configuracoes(request):
    if request.POST.get('editar_eprogModel'):
        return redirect('url_Editar_EprogModel', pk=1)

    if request.POST.get('editar_calculosModel'):
        return redirect('url_Editar_CalculosModel', pk=1)

    if request.POST.get('editar_procedimentoModel'):
        return redirect('url_Editar_ProcedimentoModel', pk=1)

    if request.POST.get('editar_sessaoModel'):
        return redirect('url_Editar_SessaoModel', pk=1)

    if request.POST.get('reset_eprogModel'):
        return redirect('url_Reset_EprogModel')

    if request.POST.get('reset_calculosModel'):
        return redirect('url_Reset_CalculosModel')

    if request.POST.get('reset_procedimentoModel'):
        return redirect('url_Reset_procedimentoModel')

    if request.POST.get('reset_sessaoModel'):
        return redirect('url_Reset_SessaoModel', pk=1)

    return render(request, "EprogApp/Entrada_configuracoes.html")

def Reset_EprogModel(request):
    # ----Resetando
    user = request.user
    banquinho = str(user)
    objeto_apagar = EprogModel.objetos.using(banquinho).all()
    for item in objeto_apagar:
        item.DuvidaComent= ''
        item.Marcador1=''
        item.Marcador2= ''
        item.Marcador3 = ''
        item.Marcador4 = ''
        item.Marcador5 = ''
        item.Acertou=''
        item.Jafoi = ''
        item.Corretas = ''
        item.Porcentagem = ''
        item.save()

    SeApagou = 'OK. Registros apagados'
    context = {
        'resultado': SeApagou
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

def Reset_CalculosModel(request):
    # ----Resetando
    user = request.user
    banquinho = str(user)
    objeto_apagar = CalculosModel.objetos.using(banquinho).get(pk=1)
    objeto_apagar.Porcentagem= '0'
    objeto_apagar.Corretas = '0'
    objeto_apagar.Incorretas = '0'
    objeto_apagar.Ordem = '0'
    objeto_apagar.apagar.save()

    SeApagou = 'OK. Registros apagados'
    context = {
        'resultado': SeApagou
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

def Reset_ProcedimentoModel(request):
    # ----Resetando
    user = request.user
    banquinho = str(user)
    objeto_apagar = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_apagar.SessaoAtual= '1'
    objeto_apagar.save()


    SeApagou = 'OK. Registros apagados'
    context = {
        'resultado': SeApagou
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

def Reset_SessaoModel(request, pk):
    user = request.user
    banquinho = str(user)
    SessaoModel.objetos.using(banquinho).all().delete()
    SessaoModel.objetos.using(banquinho).get_or_create(pk='1')
    #objeto_saida = SessaoModel.objetos.using(banquinho).get_or_create(pk='1')
    #objeto_saida = SessaoModel.objetos.using(banquinho).last()
    #objeto_saida.pk = None
    """
    objeto_saida.id = 1
    objeto_saida.save()
    #-------gravar saida default
    objeto_saida.sessao = '1'
    objeto_saida.Participante= user
    objeto_saida.save()
    """


    """
    #objeto_saida= SessaoModel.objetos.using(banquinho).all().delete()
    #objeto_saida.save()
    objeto_novo = SessaoModel.objetos.using(banquinho).get_or_create(id='1')
    objeto_novo.save()
    #objeto_novo = BlocoSaidaModel.objetos.using(banquinho).get_or_create(id='1')
    #objeto_saida = SessaoModel.objetos.using(banquinho).last()
    #n_saida_ultimo = objeto_saida.id
    #pk_next = n_saida_ultimo + 1
    #objeto_saida.pk = None
    #objeto_novo.pk = 1
    #objeto_saida.id= 1
    objeto_novo.sessao = '1'
    objeto_novo.save()
    # -------gravar saida default
    """
    SeApagou = 'OK. Registros apagados'
    context = {
        'resultado': SeApagou
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

@staff_member_required
def Entrada_relatorios(request):
    user = request.user
    banquinho = str(user)
    if request.POST.get('export'):
        #listax = SessaoModel.objetos.using(banquinho).all()
        #listax = SessaoModel.objetos.using(banquinho).values()
        listax= SessaoModel.objetos.using(banquinho).values_list(
            'Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent', )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(['Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent'])
        for item in listax:
            print(item)
            writer = csv.writer(response)
            writer.writerow([item])
        return response
    return render(request, "EprogApp/Entrada_relatorios.html")

def Entrada_sobre(request):
    return render(request, "EprogApp/Entrada_sobre.html")

#def agora(request):
#    agorinha = datetime.datetime.now()
    #msg = f'Hoje eh {agorinha}'
#    return HttpResponse(msg, content_type='text/plain')

def sominha(request):
    if request.POST.get('responder'):
        val1 = int(request.POST.get('num1'))
        val2 = int(request.POST.get('num2'))
        res = val1 + val2
        return render(request, "EprogApp/sominha.html", {'Resultado': res, 'val1': val1, 'val2': val2})
    val1= 0
    val2= 0
    res= 0
    return render(request, "EprogApp/sominha.html", {'Resultado': res, 'val1': val1, 'val2': val2})

def chamado(request):
    chamando = 'Oi, pessoas'
    chamando_ali = 'Oi, gente ali'
    valor_a= 3
    valor_b= 5
    sominha= valor_a + valor_b
    return render(request, 'EprogApp/chamado.html',
                  {'chamando': chamando, 'chamando_ali': chamando_ali, 'sominha': sominha})

#@login_required
def listagem(request):
    context = {}
    banquinho= 'eprog_p1'
    #lista = EprogModel.objetos.using(banquinho).all()
    lista= EprogModel.objetos.all()

    if request.POST.get('comecar_sessao'):
        campo = 'id'
        obj = EprogModel.objetos.last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar', pk=n_rand)

    context = {
            'lista': lista,
        }
    return render(request, 'EprogApp/listagem.html', context)

def entrada(request):
    user = request.user
    banquinho = str(user)
    if request.POST.get('comecar_sessao'):
        campo = 'id'
        obj = EprogModel.objetos.using(banquinho).last()

        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar', pk=n_rand)

    context = {
            #'lista': lista,
        }
    return render(request, 'EprogApp/Entrada.html', context)


def criar(request):
    data = {}
    form = EprogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'EprogApp/principal_vazio.html', data)

def delete(request, pk):
    user = request.user
    banquinho = str(user)
    lista = EprogModel.objetos.using('banquinho').get(pk=pk)
    lista.delete()
    return redirect('url_listagem')

def principal_hidden(request, pk):
    data = {}
    objetinho = EprogModel.objetos.get(pk=pk)
    form = EprogForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Resposta'):
        return redirect('url_principal', pk)
    data['form'] = form
    data['objetinho'] = objetinho
    return render(request, 'EprogApp/principal_hidden.html', data)

@login_required
def comecar_sessao_view(request):
    context = {}
    user = request.user
    banquinho = str(user)
    #objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    n_tentativa = objetinho_sessao.NTopico
    objetinho = EprogModel.objetos.using(banquinho).get(pk=n_tentativa)
    form = EprogForm(request.POST or None, instance=objetinho)
    objeto_procedimento = ProcedimentoModel.objetos.get(pk=1)


    if request.POST.get('comecar_sessao'):
        context = {}
        user = request.user
        banquinho = str(user)
        obj = EprogModel.objetos.using(banquinho).last()
        objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
        n_tentativa = objetinho_sessao.NTopico
        #data = {}
        #pk = n_tentativa
        objetinho = EprogModel.objetos.using('banquinho').get(pk=n_tentativa)
        form = EprogForm(request.POST or None, instance=objetinho)
        #data['form'] = form
        #data['objetinho'] = objetinho
        context = {
            'objetinho_sessao': objetinho_sessao,
            "form": form,
            "objetinho": objetinho,
            #"objetinho2": objetinho2
        }
        return redirect('url_principal', pk= n_tentativa)
        #return redirect('url_principal', context)
        #return render(request,'url_sessao', context)
        #return render(request, 'EprogApp/sessao.html', data)

    context = {
        "objetinho_sessao": objetinho_sessao,
        "form": form,
        "objetinho": objetinho,
        "n_tentativa": n_tentativa
    }
    return render(request, "EprogApp/comecar_sessao.html", context)

#@login_required
def principal(request, pk):
    data = {}
    objetinho = EprogModel.objetos.get(pk=pk)
    objetinho2 = CalculosModel.objetos.get(pk=1)
    objetinho_ordem = CalculosModel.objetos.get(pk=1)
    objetinho_sessao = SessaoModel.objetos.get(pk=1)
    n_tentativa = objetinho_sessao.NTopico

    form = EprogForm(request.POST or None, instance=objetinho)

    if request.POST.get('Listagem'):
        return redirect('url_listagem')

    if request.POST.get('Novo'):
        return redirect('url_criar')

    if request.POST.get('Salvar'):
        data = {}
        objetinho = EprogModel.objetos.using('banquinho').get(pk=pk)
        form = EprogForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página

        data['form'] = form
        data['objetinho'] = objetinho
        return render(request, 'EprogApp/principal.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_listagem')

    if request.POST.get('primeiro'):
        n = 1
        return redirect('url_principal', pk=n)

    if request.POST.get('proximo'):
        campo = 'id'
        obj_ultimo = EprogModel.objetos.using('banquinho').last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = EprogModel.objetos.using('banquinho').get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_principal', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = EprogModel.objetos.using('banquinho').get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_principal', pk=n)

    if request.POST.get('Testar'):
        campo = 'id'
        obj = EprogModel.objetos.using('banquinho').last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_principal_hidden', pk=n_rand)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = EprogModel.objetos.using('banquinho').last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_principal', pk=n)

    if request.POST.get('Correta'):
        objetinho = EprogModel.objetos.using('banquinho').get(pk=pk)
        #objetinho.Acertou = '1'
        #objetinho.save()

        form = EprogForm(request.POST or None, instance=objetinho)

        objetinho2 = CalculosModel.objetos.get(pk=1)
        ordem_atual = objetinho2.Ordem
        ordem_next = ordem_atual + 1
        objetinho2.Ordem = ordem_next
        objetinho2.save()
        nn = objetinho2.Ordem

        # objetinho_tcorretas = CalculosModel.objetos2.get(pk=1)
        # totalcorretas = int(objetinho_tcorretas.Corretas)
        # totalcorretas += 1
        # objetinho_tcorretas.Corretas = totalcorretas
        # objetinho_tcorretas.save()
        # objetinho2 = CalculosModel.objetos2.get(pk=1)
        objetinho_sessao_atual = SessaoModel.objetos.using('banquinho').get(pk=nn)
        NTopico_next = objetinho_sessao_atual.NTopico
        #ordem_atual = objetinho_sessao_atual.Ordem
        #ordem_atual += 1
        #objetinho_sessao_next = SessaoModel.objeto_sessao.get(pk=ordem_atual)

        context = {
            "form": form,
            "objetinho": objetinho,
            #"objetinho2": objetinho2,
            "objetinho_sessao": objetinho_sessao_atual,
            "n_tentativa": NTopico_next
            }
        #return render("EprogApp/principal.html", context)
        return redirect('url_principal', pk= NTopico_next)


    context = {
        "form": form,
        "objetinho": objetinho,
        "objetinho2": objetinho2,
        "objetinho_ordem": objetinho_ordem,
        #"objetinho_sessao": objetinho_sessao,
        "n_tentativa": n_tentativa
    }
    return render(request, "EprogApp/principal.html", context)

#@login_required
def update(request, pk):
    data = {}
    objetinho = EprogModel.objetos.get(pk=pk)
    objetinho2 = CalculosModel.objetos.get(pk=1)
    objetinho_ordem = CalculosModel.objetos.get(pk=1)
    objetinho_sessao = SessaoModel.objetos.get(pk=1)
    #n_tentativa = objetinho_sessao.NTopico

    form = EprogForm(request.POST or None, instance=objetinho)

    if request.POST.get('Listagem'):
        return redirect('url_listagem')

    if request.POST.get('Novo'):
        return redirect('url_criar')

    if request.POST.get('Salvar_update'):
        data = {}
        objetinho = EprogModel.objetos.get(pk=pk)
        form = EprogForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página

        data['form'] = form
        data['objetinho'] = objetinho
        return render(request, 'EprogApp/update.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_listagem')

    if request.POST.get('primeiro_update'):
        n = 1
        return redirect('url_update', pk=n)

    if request.POST.get('proximo_update'):
        campo = 'id'
        obj_ultimo = EprogModel.objetos.last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = EprogModel.objetos.get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_update', pk=n)

    if request.POST.get('anterior_update'):
        campo = 'id'
        obj = EprogModel.objetos.get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_update', pk=n)

    if request.POST.get('Testar'):
        campo = 'id'
        obj = EprogModel.objetos.last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_principal_hidden', pk=n_rand)

    if request.POST.get('ultimo_update'):
        campo = 'id'
        obj = EprogModel.objetos.last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_update', pk=n)

    if request.POST.get('Correta'):

        objetinho = EprogModel.objetos.get(pk=pk)
        form = EprogForm(request.POST or None, instance=objetinho)

        objetinho2 = CalculosModel.objetos.get(pk=1)
        ordem_atual = objetinho2.Ordem
        ordem_next = ordem_atual + 1
        objetinho2.Ordem = ordem_next
        objetinho2.save()
        nn = objetinho2.Ordem

        # objetinho_tcorretas = CalculosModel.objetos2.get(pk=1)
        # totalcorretas = int(objetinho_tcorretas.Corretas)
        # totalcorretas += 1
        # objetinho_tcorretas.Corretas = totalcorretas
        # objetinho_tcorretas.save()
        # objetinho2 = CalculosModel.objetos2.get(pk=1)
        objetinho_sessao_atual = SessaoModel.objetos.get(pk=nn)
        NTopico_next = objetinho_sessao_atual.NTopico
        #ordem_atual = objetinho_sessao_atual.Ordem
        #ordem_atual += 1
        #objetinho_sessao_next = SessaoModel.objeto_sessao.get(pk=ordem_atual)

        context = {
            "form": form,
            "objetinho": objetinho,
            #"objetinho2": objetinho2,
            "objetinho_sessao": objetinho_sessao_atual,
            "n_tentativa": NTopico_next
            }
        #return render("EprogApp/principal.html", context)
        return redirect('url_update', pk= NTopico_next)


    context = {
        "form": form,
        "objetinho": objetinho,
        "objetinho2": objetinho2,
        "objetinho_ordem": objetinho_ordem,
        #"objetinho_sessao": objetinho_sessao,
        #"n_tentativa": n_tentativa
    }
    return render(request, "EprogApp/update.html", context)

@login_required
def sessao_view(request, pk):
        user = request.user
        banquinho = str(user)
        objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
        obj_linhaum = EprogModel.objetos.using(banquinho).get(pk=1)
        objeto_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
        objeto_sessaoUm = SessaoModel.objetos.using(banquinho).get(pk=1)

        form = EprogForm(request.POST or None, instance=objetinho)

        if request.POST.get('Salvar'):
            obj_linhaum = EprogModel.objetos.using(banquinho).get(pk=1)
            objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
            form = EprogForm(request.POST or None, instance=objetinho)
            if form.is_valid():
                form.save()

            context = {
                "form": form,
                "objetinho": objetinho,
                "obj_linhaum": obj_linhaum,
                # "objetinho2": objetinho2,
                "objeto_sessao": objeto_sessao
            }
            return render(request, "EprogApp/sessao.html", context)

        if request.POST.get('Testar'):
            objetX = EprogModel.objetos.using(banquinho).get(pk=pk)
            objetX.SuaResposta = ''
            objetX.save()

            campo = 'id'
            obj = EprogModel.objetos.using(banquinho).last()
            valor_campo = getattr(obj, campo)
            total = valor_campo
            n_rand = randint(1, total)
            obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou
            while SeAcertou == '1':
                n_rand = randint(1, total)
                obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
                SeAcertou = obj_sorteio.Acertou

            return redirect('url_sessao_testar', pk=n_rand)

        if request.POST.get('Sessao'):
            return redirect('url_sessao', pk=pk)

        if request.POST.get('Resposta'):
            return redirect('url_sessao', pk=pk)

        if request.POST.get('Sair'):
            # fazer o logout aqui:
             return redirect('logout')

        if request.POST.get('Upload'):
            # fazer o logout aqui:
             return redirect('url_sessao_upload', pk=pk)

        if request.POST.get('Correta'):
            Objeto_Procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
            obj_linhaum = EprogModel.objetos.using(banquinho).get(pk=1)
            objeto_sessaoUm = SessaoModel.objetos.using(banquinho).get(pk=1)
            objeto_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
            objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
            #form = EprogForm(request.POST or None, instance=objetinho)
            #if form.is_valid():
            #    form.save()
            # Bloco 1 - início
            objetinho.SuaResposta= ''
            objetinho.save()
            objetinho.Acertou = '1'
            objetinho.Jafoi = '1'
            objetinho.save()
            tcorretas = EprogModel.objetos.using(banquinho).filter(Acertou='1').count()
            obj_linhaum.Corretas = str(tcorretas)
            obj_linhaum.save()
            campo = 'id'
            obj_ult = EprogModel.objetos.using(banquinho).last()
            total_rec = getattr(obj_ult, campo)
            tporcentagem = (tcorretas/total_rec)*100
            obj_linhaum.Porcentagem = str(tporcentagem) + '%'
            if objetinho.id == 1:
                obj_linhaum.Acertou = '1'
                obj_linhaum.save()
            obj_linhaum.save()
            # Bloco 1- fim

            #Populando o arquivo de saída início
            if Objeto_Procedimento.Botao_avalia == '0':
                quantos_saida = SessaoModel.objetos.using(banquinho).count()
                pk_next = quantos_saida + 1
                objeto_saida = SessaoModel.objetos.using(banquinho).last()
                #n_saida_ultimo = objeto_saida.id
                objeto_saida.pk = None
                objeto_saida.pk = pk_next
                objeto_saida.id = pk_next
                objeto_saida.save()
                objeto_sessao = SessaoModel.objetos.using(banquinho).last()
                pk_ultimo= objeto_sessao.pk
                #objeto_sessao_ultimo = SessaoModel.objetos.using(banquinho).last()
                #pk_ultimo = pk_next
                #objeto_sessao.pk = None
                objeto_sessao.Dia = str(datetime.date.today())
                objeto_sessao.Horario = datetime.datetime.now().strftime('%H:%M:%S')
                objeto_sessao.Tentativa = pk_ultimo
                #objeto_sessao.Tentativa = pk_ultimo + 1
                objeto_sessao.Ordem = objetinho.Ordem
                objeto_sessao.Topico = objetinho.Topico
                objeto_sessao.DuvidaComent = objetinho.DuvidaComent
                objeto_sessao.Sessao = Objeto_Procedimento.SessaoAtual
                objeto_sessao.Acertou = objetinho.Acertou
                objeto_sessao.save()
                objetinho.Jafoi = '1' ## mudou de lugar
                objetinho.save()
                Objeto_Procedimento.Botao_avalia = '1'
                Objeto_Procedimento.save()
                # Populando o arquivo de saída - fim

            if tcorretas == total_rec:
                return redirect('url_parabens_view')

            #form = EprogForm(request.POST or None, instance=objetinho)
            #if form.is_valid():
            #    form.save()

            context = {
                "form": form,
                "objetinho": objetinho,
                "obj_linhaum": obj_linhaum,
                # "objetinho2": objetinho2,
                "objetinhoSessao": objeto_sessao,
                "objeto_sessaoUm": objeto_sessaoUm
            }
            return render(request, "EprogApp/sessao.html", context)

        if request.POST.get('Incorreta'):
            Objeto_Procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
            obj_linhaum = EprogModel.objetos.using(banquinho).get(pk=1)
            objeto_sessaoUm = SessaoModel.objetos.using(banquinho).get(pk=1)
            objeto_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
            objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
            # form = EprogForm(request.POST or None, instance=objetinho)
            # if form.is_valid():
            #    form.save()
            # Bloco 1 - início
            objetinho.SuaResposta = ''
            objetinho.save()
            objetinho.Acertou = '0'
            objetinho.Jafoi = '1'
            objetinho.save()
            tcorretas = EprogModel.objetos.using(banquinho).filter(Acertou='1').count()
            obj_linhaum.Corretas = str(tcorretas)
            obj_linhaum.save()
            campo = 'id'
            obj_ult = EprogModel.objetos.using(banquinho).last()
            total_rec = getattr(obj_ult, campo)
            tporcentagem = (tcorretas / total_rec) * 100
            obj_linhaum.Porcentagem = str(tporcentagem) + '%'
            if objetinho.id == 1:
                obj_linhaum.Acertou = '1'
                obj_linhaum.save()
            obj_linhaum.save()
            # Bloco 1- fim

            # Populando o arquivo de saída início
            if Objeto_Procedimento.Botao_avalia == '0':
                quantos_saida = SessaoModel.objetos.using(banquinho).count()
                pk_next = quantos_saida + 1
                objeto_saida = SessaoModel.objetos.using(banquinho).last()
                # n_saida_ultimo = objeto_saida.id
                objeto_saida.pk = None
                objeto_saida.pk = pk_next
                objeto_saida.id = pk_next
                objeto_saida.save()
                objeto_sessao = SessaoModel.objetos.using(banquinho).last()
                pk_ultimo = objeto_sessao.pk
                # objeto_sessao_ultimo = SessaoModel.objetos.using(banquinho).last()
                # pk_ultimo = pk_next
                # objeto_sessao.pk = None
                objeto_sessao.Dia = str(datetime.date.today())
                objeto_sessao.Horario = datetime.datetime.now().strftime('%H:%M:%S')
                objeto_sessao.Tentativa = pk_ultimo
                # objeto_sessao.Tentativa = pk_ultimo + 1
                objeto_sessao.Ordem = objetinho.Ordem
                objeto_sessao.Topico = objetinho.Topico
                objeto_sessao.DuvidaComent = objetinho.DuvidaComent
                objeto_sessao.Sessao = Objeto_Procedimento.SessaoAtual
                objeto_sessao.Acertou = objetinho.Acertou
                objeto_sessao.save()
                objetinho.Jafoi = '1'  ## mudou de lugar
                objetinho.save()
                Objeto_Procedimento.Botao_avalia = '1'
                Objeto_Procedimento.save()
                # Populando o arquivo de saída - fim

            if tcorretas == total_rec:
                return redirect('url_parabens_view')

            # form = EprogForm(request.POST or None, instance=objetinho)
            # if form.is_valid():
            #    form.save()

            context = {
                "form": form,
                "objetinho": objetinho,
                "obj_linhaum": obj_linhaum,
                # "objetinho2": objetinho2,
                "objetinhoSessao": objeto_sessao,
                "objeto_sessaoUm": objeto_sessaoUm
            }
            return render(request, "EprogApp/sessao.html", context)

        context = {
            "form": form,
            "objetinho": objetinho,
            "obj_linhaum": obj_linhaum,
            # "objetinho2": objetinho2,
            "objeto_sessao": objeto_sessao,
            "objeto_sessaoUm": objeto_sessaoUm
            }
        return render(request, "EprogApp/sessao.html", context)

@login_required
def sessao_testar(request, pk):
    user = request.user
    banquinho = str(user)
    # data = {}
    Objeto_Procedimento= ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    Objeto_Procedimento.Botao_avalia= '0'
    Objeto_Procedimento.save()
    objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    # objetinho2 = CalculosModel.objetos2.get(pk=1)
    objetinhoSessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    form = EprogForm(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
        form = EprogForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
        return redirect('url_sessao', pk=pk)

    context = {
        "form": form,
        "objetinho": objetinho,
        # "objetinho2": objetinho2,
        "objetinhoSessao": objetinhoSessao
    }
    return render(request, "EprogApp/sessao_testar.html", context)

