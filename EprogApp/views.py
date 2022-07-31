from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
import datetime
import csv
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from random import randint
from django.contrib.auth.decorators import login_required
from .models import EprogModel, CalculosModel, SessaoModel, ProcedimentoModel, PretesteModel, PostesteModel, \
    ModulosModel
from .forms import EprogForm, CalculosForm, SessaoForm, ProcedimentoForm, ImageForm, \
    PretesteForm2, PostesteForm, \
    PretesteForm_executar, Entrada_ExperimentadorForm, Editar_ModulosForm

def Entrada_Experimentador_view(request):
    user = request.user
    banquinho = str(user)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    senha_mesmo = objeto_procedimento.Senha_Experimentador
    senha_entrou = objeto_procedimento.Senha_Salva
    if senha_entrou == senha_mesmo:
        print('sim, acertou')
        return redirect('url_Entrada_configuracoes')

    form = Entrada_ExperimentadorForm(request.POST or None, instance=objeto_procedimento)

    if request.POST.get('voltar'):
        return redirect('url_entrada')

    if request.POST.get('entrar'):
        objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
        form = Entrada_ExperimentadorForm(request.POST or None, instance=objeto_procedimento)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'objeto_procedimento': objeto_procedimento,
            }
            return render(request, 'EprogApp/Entrada_experimentador.html', context)

    context = {'form': form, 'objeto_procedimento': objeto_procedimento}

    return render(request, 'EprogApp/Entrada_experimentador.html', context)

def sessao_upload(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    #objetinho = EprogModel.objetos.get(pk=pk)
    form = EprogForm(request.POST or None, instance=objetinho)

    # ESTÁ DESATIVADO. NÃO POSSO DEIXAR O PARTICIPANTE CARREGAR FIGURAS...
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
        return redirect('url_Entrada_configuracoes')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_EprogModel.html', context)

def Editar_Preteste(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = PretesteModel.objetos.using(banquinho).get(pk=pk)
    form = PretesteForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = PretesteModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = PretesteModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Participante = ' '
        objeto_novo.Ordem = pk_next
        objeto_novo.Modulo = ' '
        objeto_novo.Acertou = ' '
        objeto_novo.Jafoi = ' '
        objeto_novo.Questao = ' '
        objeto_novo.Alternativa_A = ' '
        objeto_novo.Alternativa_B = ' '
        objeto_novo.Alternativa_C = ' '
        objeto_novo.Alternativa_D = ' '
        objeto_novo.Alternativa_E = ' '
        objeto_novo.Alternativa_X = ' '
        objeto_novo.Alternativa_A_escolhida = ' '
        objeto_novo.Alternativa_B_escolhida = ' '
        objeto_novo.Alternativa_C_escolhida = ' '
        objeto_novo.Alternativa_D_escolhida = ' '
        objeto_novo.Alternativa_E_escolhida = ' '
        objeto_novo.Escolheu = ' '
        objeto_novo.save()
        return redirect('url_Editar_Preteste', pk=pk_next)

    if request.POST.get('Salvar'):
        data = {}
        objetinho = PretesteModel.objetos.using(banquinho).get(pk=pk)
        form = PretesteForm2(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_Preteste.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_Preteste', pk=1)

    if request.POST.get('primeiro'):
        return redirect('url_Editar_Preteste', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = PretesteModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = PretesteModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_Preteste', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = PretesteModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_Preteste', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = PretesteModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_Preteste', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_configuracoes')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_Preteste.html', context)

def Editar_Posteste(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = PostesteModel.objetos.using(banquinho).get(pk=pk)
    form = PostesteForm(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = PostesteModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = PostesteModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Participante = ' '
        objeto_novo.Ordem = pk_next
        objeto_novo.Modulo = ' '
        objeto_novo.Acertou = ' '
        objeto_novo.Jafoi = ' '
        objeto_novo.Questao = ' '
        objeto_novo.Alternativa_A = ' '
        objeto_novo.Alternativa_B = ' '
        objeto_novo.Alternativa_C = ' '
        objeto_novo.Alternativa_D = ' '
        objeto_novo.Alternativa_E = ' '
        objeto_novo.Alternativa_X = ' '
        objeto_novo.Alternativa_A_escolhida = ' '
        objeto_novo.Alternativa_B_escolhida = ' '
        objeto_novo.Alternativa_C_escolhida = ' '
        objeto_novo.Alternativa_D_escolhida = ' '
        objeto_novo.Alternativa_E_escolhida = ' '
        objeto_novo.Escolheu = ' '
        objeto_novo.save()
        return redirect('url_Editar_Posteste', pk=pk_next)

    if request.POST.get('Salvar'):
        data = {}
        objetinho = PostesteModel.objetos.using(banquinho).get(pk=pk)
        form = PostesteForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_Posteste.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_Posteste', pk=1)

    if request.POST.get('primeiro'):
        return redirect('url_Editar_Posteste', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = PostesteModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = PostesteModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_Posteste', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = PostesteModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_Posteste', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = PostesteModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_Posteste', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_configuracoes')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_Posteste.html', context)

def Editar_Modulos_view(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = ModulosModel.objetos.using(banquinho).get(pk=pk)
    form = Editar_ModulosForm(request.POST or None, instance=objetinho)

    if request.POST.get('Novo'):
        user = request.user
        banquinho = str(user)
        objeto_ultimo = ModulosModel.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = ModulosModel.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.NoModulo = pk_next
        objeto_novo.Ordem = pk_next
        objeto_novo.Descricao = ''
        objeto_novo.Treino_Primeiro = 0
        objeto_novo.Treino_Ultimo = 0
        objeto_novo.PreTeste_Primeiro = 0
        objeto_novo.PreTeste_Ultimo = 0
        objeto_novo.TemPosTeste = 0
        objeto_novo.PosTeste_Primeiro = 0
        objeto_novo.PosTeste_Ultimo = 0
        objeto_novo.Treino_Acesso = '1'
        objeto_novo.PreTeste_Acesso = '1'
        objeto_novo.PosTeste_Acesso = '1'
        objeto_novo.save()
        return redirect('url_Editar_Modulos', pk=pk_next)

    if request.POST.get('Salvar'):
        data = {}
        objetinho = ModulosModel.objetos.using(banquinho).get(pk=pk)
        form = Editar_ModulosForm(request.POST or None, instance=objetinho)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'EprogApp/Editar_Modulos.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_Editar_Modulos', pk=1)

    if request.POST.get('primeiro'):
        return redirect('url_Editar_Modulos', pk=1)

    if request.POST.get('proximo'):
        campo = 'id'
        user = request.user
        banquinho = str(user)
        obj_ultimo = ModulosModel.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = ModulosModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = 1
        return redirect('url_Editar_Modulos', pk=n)

    if request.POST.get('anterior'):
        campo = 'id'
        obj = ModulosModel.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = 1
        return redirect('url_Editar_Modulos', pk=n)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = ModulosModel.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_Editar_Modulos', pk=n)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_configuracoes')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_Modulos.html', context)


def Editar_CalculosModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = CalculosModel.objetos.using(banquinho).get(pk=pk)
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
        return redirect('url_Entrada_configuracoes')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_CalculosModel.html', context)

def Editar_ProcedimentoModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = ProcedimentoModel.objetos.using(banquinho).get(pk=pk)
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
        return redirect('url_Entrada_configuracoes')

    context={
        'form': form,
        'objetinho': objetinho,
    }
    return render(request, 'EprogApp/Editar_ProcedimentoModel.html', context)

def Editar_SessaoModel(request, pk):
    user = request.user
    banquinho = str(user)
    objetinho = SessaoModel.objetos.using(banquinho).get(pk=pk)
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
        return redirect('url_Entrada_configuracoes')

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
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_ProcedimentoModel = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    x_ModuloAntigo = objeto_procedimento.ModuloAntigo
    objeto_modulos = ModulosModel.objetos.using(banquinho).get(pk=x_ModuloAntigo)

    X_modulo_atual = x_ModuloAntigo
    x_ModuloFinal = objeto_procedimento.ModuloFinal
    n_ModuloFinal = int(x_ModuloFinal)
    form_procedimento = ProcedimentoForm(request.POST or None, instance=objeto_procedimento)
    qual_etapa = objeto_procedimento

    campo = 'id'
    obj = EprogModel.objetos.using(banquinho).last()
    valor_campo = getattr(obj, campo)
    total = valor_campo

    n_rand = randint(1, total)
    obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
    SeAcertou = obj_sorteio.Acertou
    qualmodulo = objeto_procedimento.ModuloAtual
    modulo_sorteado = obj_sorteio.Modulo

    x_AgoraTreino = objeto_procedimento.AgoraTreino


    if objeto_procedimento.FimUltimoModulo == '1':
        return redirect('url_sessao_fim_modulo_final', pk=1)

    x_ModuloAntigo = objeto_procedimento.ModuloAntigo
    x_moduloatual = x_ModuloAntigo
    x_ativada = obj_sorteio.Ativada

    if x_AgoraTreino == '1':
        while SeAcertou == '1' or qualmodulo != modulo_sorteado or x_ativada == '0':
            n_rand = randint(1, total)
            obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou
            modulo_sorteado = obj_sorteio.Modulo
            x_ativada = obj_sorteio.Ativada

    if request.POST.get('comecar_algo'):
        objeto_procedimento.ModuloAtual = objeto_procedimento.ModuloAntigo
        objeto_procedimento.Retreino = '0'
        objeto_procedimento.save()
        x_ModuloAntigo = objeto_procedimento.ModuloAntigo
        x_moduloatual = x_ModuloAntigo
        n_ModuloAntigo = int(x_ModuloAntigo)
        objeto_modulos = ModulosModel.objetos.using(banquinho).get(pk=n_ModuloAntigo)
        x_Modulo_EtapaAtual = objeto_modulos.Modulo_EtapaAtual
        print('Modulo_EtapaAtual agora é:', x_Modulo_EtapaAtual)

        x_Treino_Acesso = objeto_modulos.Treino_Acesso
        x_PreTeste_Acesso = objeto_modulos.PreTeste_Acesso
        x_PosTeste_Acesso = objeto_modulos.PosTeste_Acesso

        x_Treino_Primeiro = objeto_modulos.Treino_Acesso
        x_PreTeste_Primeiro = objeto_modulos.PreTeste_Primeiro
        n_PreTeste_Primeiro = int(x_PreTeste_Primeiro)
        x_PosTeste_Primeiro = objeto_modulos.PosTeste_Primeiro
        n_PosTeste_Primeiro = int(x_PosTeste_Primeiro)

        x_TemPosTeste = objeto_modulos.TemPosTeste
        x_Modulo_EtapaAtual = objeto_modulos.Modulo_EtapaAtual

        if x_Modulo_EtapaAtual == '1' and x_PreTeste_Acesso == '1':
            return redirect('url_Preteste2', pk=n_PreTeste_Primeiro)

        if x_Modulo_EtapaAtual == '1' and x_PreTeste_Acesso == '0':
            return redirect('url_Entrada_Iniciar_Indisponivel')

        if x_Modulo_EtapaAtual == '2' and x_Treino_Acesso == '1':
            return redirect('url_sessao_testar', pk=n_rand)
        if x_Modulo_EtapaAtual == '2' and x_Treino_Acesso == '0':
            return redirect('url_Entrada_Iniciar_Indisponivel')

        if x_Modulo_EtapaAtual == '3' and x_PosTeste_Acesso == '1':
            return redirect('url_Posteste', pk=x_PosTeste_Primeiro)
        if x_Modulo_EtapaAtual == '3' and x_PosTeste_Acesso == '0':
            return redirect('url_Entrada_Iniciar_Indisponivel')

    if request.POST.get('comecar_retreino'):
        objeto_procedimento.ModuloAtual = objeto_procedimento.ModuloAntigo
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Retreino')

    context = {
        "objetinho_sessao": objetinho_sessao,
        "objeto_ProcedimentoModel": objeto_ProcedimentoModel,
        "objeto_modulos": objeto_modulos,
        "form_procedimento": form_procedimento
    }
    return render(request, "EprogApp/Entrada_Iniciar2.html", context)

@login_required
def Entrada_Iniciar_Indisponivel(request):
    user = request.user
    banquinho = str(user)
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_ProcedimentoModel = ProcedimentoModel.objetos.using(banquinho).get(pk=1)

    context = {
        "objetinho_sessao": objetinho_sessao,
        "objeto_procedimento": objeto_procedimento,

        # "form": form,
        #"objetinho": objetinho,
        #"n_tentativa": n_tentativa
    }
    return render(request, "EprogApp/Entrada_iniciar_Indisponivel.html", context)

@login_required
def Entrada_Retreino_view(request):
    user = request.user
    banquinho = str(user)
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_modulo1 = ModulosModel.objetos.using(banquinho).get(pk=1)
    objeto_modulo2 = ModulosModel.objetos.using(banquinho).get(pk=2)
    objeto_modulo3 = ModulosModel.objetos.using(banquinho).get(pk=3)
    objeto_modulo4 = ModulosModel.objetos.using(banquinho).get(pk=4)
    objeto_modulo5 = ModulosModel.objetos.using(banquinho).get(pk=5)
    objeto_modulo6 = ModulosModel.objetos.using(banquinho).get(pk=6)
    objeto_modulo7 = ModulosModel.objetos.using(banquinho).get(pk=7)
    objeto_modulo8 = ModulosModel.objetos.using(banquinho).get(pk=8)
    objeto_modulo9 = ModulosModel.objetos.using(banquinho).get(pk=9)
    objeto_modulo10 = ModulosModel.objetos.using(banquinho).get(pk=10)
    objeto_modulo11 = ModulosModel.objetos.using(banquinho).get(pk=11)
    objeto_modulo12 = ModulosModel.objetos.using(banquinho).get(pk=12)
    objeto_modulo13 = ModulosModel.objetos.using(banquinho).get(pk=13)
    objeto_modulo14 = ModulosModel.objetos.using(banquinho).get(pk=14)
    objeto_modulo15 = ModulosModel.objetos.using(banquinho).get(pk=15)

    x_Descricao1 = objeto_modulo1
    x_Descricao2 = objeto_modulo2
    x_Descricao3 = objeto_modulo3
    x_Descricao4 = objeto_modulo4
    x_Descricao5 = objeto_modulo5
    x_Descricao6 = objeto_modulo6
    x_Descricao7 = objeto_modulo7
    x_Descricao8 = objeto_modulo8
    x_Descricao9 = objeto_modulo9
    x_Descricao10 = objeto_modulo10
    x_Descricao11 = objeto_modulo11
    x_Descricao12 = objeto_modulo12
    x_Descricao13 = objeto_modulo13
    x_Descricao14 = objeto_modulo14
    x_Descricao15 = objeto_modulo15

    #lista = EprogModel.objetos.using(banquinho).all()
    x_ModuloAntigo = objeto_procedimento.ModuloAntigo
    n_ModuloAntigo = int(x_ModuloAntigo)
    x_ModuloFinal = objeto_procedimento.ModuloFinal
    n_ModuloFinal = int(x_ModuloFinal)

    if request.POST.get('Módulo1'):
        objeto_procedimento.ModuloAtual = '1'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo2'):
        if n_ModuloAntigo > 2:
            objeto_procedimento.ModuloAtual = '2'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo3'):
        if n_ModuloAntigo > 3:
            objeto_procedimento.ModuloAtual = '3'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo4'):
        if n_ModuloFinal > 4:
            objeto_procedimento.ModuloAtual = '4'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo5'):
        if n_ModuloAntigo > 5:
            objeto_procedimento.ModuloAtual = '5'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo6'):
        if n_ModuloAntigo > 6:
            objeto_procedimento.ModuloAtual = '6'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo7'):
        if n_ModuloAntigo > 7:
            objeto_procedimento.ModuloAtual = '7'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo8'):
        if n_ModuloAntigo > 8:
            objeto_procedimento.ModuloAtual = '8'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo9'):
        if n_ModuloAntigo > 9:
            objeto_procedimento.ModuloAtual = '9'
            objeto_procedimento.Retreino = '1'
            objeto_procedimento.save()
            return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo10'):
        objeto_procedimento.ModuloAtual = '10'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo11'):
        objeto_procedimento.ModuloAtual = '11'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo12'):
        objeto_procedimento.ModuloAtual = '12'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo13'):
        objeto_procedimento.ModuloAtual = '13'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo14'):
        objeto_procedimento.ModuloAtual = '14'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo15'):
        objeto_procedimento.ModuloAtual = '15'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo16'):
        objeto_procedimento.ModuloAtual = '16'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo17'):
        objeto_procedimento.ModuloAtual = '17'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo18'):
        objeto_procedimento.ModuloAtual = '18'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo19'):
        objeto_procedimento.ModuloAtual = '19'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('Módulo20'):
        objeto_procedimento.ModuloAtual = '20'
        objeto_procedimento.Retreino = '1'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    if request.POST.get('comecar_sessao'):
        objeto_procedimento.ModuloAtual = objeto_procedimento.ModuloAntigo
        objeto_procedimento.Retreino = '0'
        objeto_procedimento.save()
        return redirect('url_Entrada_Iniciar_Retreino')

    context = {
        "objetinho_sessao": objetinho_sessao,
        "objeto_procedimento": objeto_procedimento,
        "objeto_modulo1": objeto_modulo1,
        "objeto_modulo2": objeto_modulo2,
        "objeto_modulo3": objeto_modulo3,
        "objeto_modulo4": objeto_modulo4,
        "objeto_modulo5": objeto_modulo5,
        "objeto_modulo6": objeto_modulo6,
        "objeto_modulo7": objeto_modulo7,
        "objeto_modulo8": objeto_modulo8,
        "objeto_modulo9": objeto_modulo9,
        "objeto_modulo10": objeto_modulo10,
        "objeto_modulo11": objeto_modulo11,
        "objeto_modulo12": objeto_modulo12,
        "objeto_modulo13": objeto_modulo13,
        "objeto_modulo14": objeto_modulo14,
        "objeto_modulo15": objeto_modulo15

        # "form": form,
        #"objetinho": objetinho,
        #"n_tentativa": n_tentativa
    }
    return render(request, "EprogApp/Entrada_retreino.html", context)

@login_required
def Entrada_Iniciar_Normal(request):
    user = request.user
    banquinho = str(user)
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)

    # mudar sessao - inicio
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    SessaoAntiga = objeto_procedimento.SessaoAtual
    n_SessaoAntiga = int(SessaoAntiga)
    n_SessaoAtual = n_SessaoAntiga + 1
    objeto_procedimento.SessaoAtual = str(n_SessaoAtual)
    objeto_procedimento.Retreino = '0'
    objeto_procedimento.save()
    objetinho_sessao.Sessao = objeto_procedimento.SessaoAtual
    objetinho_sessao.save()
    # mudar sessao - fim

    campo = 'id'
    obj = EprogModel.objetos.using(banquinho).last()
    valor_campo = getattr(obj, campo)
    total = valor_campo

    n_rand = randint(1, total)
    obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
    qualmodulo = objeto_procedimento.ModuloAtual
    modulo_sorteado = obj_sorteio.Modulo

    while not qualmodulo == modulo_sorteado:
        # while SeAcertou == '1' and not (qualmodulo == modulo_sorteado):
        n_rand = randint(1, total)
        obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
        modulo_sorteado = obj_sorteio.Modulo
        if modulo_sorteado == qualmodulo:
            return redirect('url_sessao_testar', pk=n_rand)

    context = {
        "objetinho_sessao": objetinho_sessao,
        "objeto_procedimento": objeto_procedimento,
    }
    return render(request, "EprogApp/Entrada_iniciar_normal.html", context)

@login_required
def entrada_iniciar_retreino(request):
    user = request.user
    banquinho = str(user)
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)

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
    obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
    qualmodulo = objeto_procedimento.ModuloAtual
    modulo_sorteado = obj_sorteio.Modulo

    while not qualmodulo == modulo_sorteado:
        # while SeAcertou == '1' and not (qualmodulo == modulo_sorteado):
        n_rand = randint(1, total)
        obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
        modulo_sorteado = obj_sorteio.Modulo
        print('sorteamos o módulo ', modulo_sorteado)
        if modulo_sorteado == qualmodulo:
            return redirect('url_sessao_testar', pk=n_rand)

    context = {
        "objetinho_sessao": objetinho_sessao,
        "objeto_procedimento": objeto_procedimento,
    }
    return render(request, "EprogApp/Entrada_retreino.html", context)

@staff_member_required
def Entrada_configuracoes(request):
    user = request.user
    banquinho = str(user)
    objeto_procedimento = objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento.Senha_Salva = 'xxxx'
    objeto_procedimento.save()
    form_procedimento = ProcedimentoForm(request.POST or None, instance=objeto_procedimento)

    if request.POST.get('editar_eprogModel'):
        return redirect('url_Editar_EprogModel', pk=1)

    if request.POST.get('editar_preteste'):
        return redirect('url_Editar_Preteste', pk=1)

    if request.POST.get('editar_posteste'):
        return redirect('url_Editar_Posteste', pk=1)

    if request.POST.get('editar_calculosModel'):
        return redirect('url_Editar_CalculosModel', pk=1)

    if request.POST.get('editar_modulos'):
        return redirect('url_Editar_Modulos', pk=1)

    if request.POST.get('relatorios'):
        return redirect('url_Entrada_relatorios')

    if request.POST.get('editar_procedimentoModel'):
        return redirect('url_Editar_ProcedimentoModel', pk=1)

    if request.POST.get('Editar_EtapasAcesso'):
        return redirect('url_Editar_EtapasAcesso', pk=1)

    if request.POST.get('editar_sessaoModel'):
        return redirect('url_Editar_SessaoModel', pk=1)

    if request.POST.get('reset_models'):
        return redirect('url_reset_models')

    if request.POST.get('reset_eprogModel'):
        return redirect('url_Reset_EprogModel')

    if request.POST.get('reset_calculosModel'):
        return redirect('url_Reset_CalculosModel')

    if request.POST.get('reset_procedimentoModel'):
        return redirect('url_Reset_ProcedimentoModel')

    if request.POST.get('reset_sessaoModel'):
        return redirect('url_Reset_SessaoModel', pk=1)

    if request.POST.get('preteste'):
        return redirect('url_Preteste2', pk=1)

    if request.POST.get('Salvar'):
        if form_procedimento.is_valid():
            form_procedimento.save()

        context = {
            "objeto_procedimento": objeto_procedimento,
            "form_procedimento": form_procedimento
        }
        return redirect('url_Entrada_Iniciar')

    context = {
        "objeto_procedimento": objeto_procedimento,
        "form_procedimento": form_procedimento
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

def Reset_Models(request):
    # ----Resetando
    user = request.user
    banquinho = str(user)

    ##### RESETANDO EPROGMODEL #######
    objeto_apagarEprogModel = EprogModel.objetos.using(banquinho).all()
    for item in objeto_apagarEprogModel:
        item.DuvidaComent= ''
        item.Marcador1=''
        item.Marcador2= ''
        item.Marcador3 = ''
        item.Marcador4 = ''
        item.Marcador5 = ''
        item.Acertou= '0'
        item.Jafoi = '0'
        item.Corretas = '0'
        item.Porcentagem = '0'
        item.save()

    ##### RESETANDO PRETESTEMODEL #######
    objeto_apagarPretesteModel = PretesteModel.objetos.using(banquinho).all()
    for item in objeto_apagarPretesteModel:
        item.Alternativa_A_escolhida = ''
        item.Alternativa_B_escolhida = ''
        item.Alternativa_C_escolhida = ''
        item.Alternativa_D_escolhida = ''
        item.Alternativa_E_escolhida = ''
        item.Escolheu = ''
        item.save()

    ##### RESETANDO POSTESTEMODEL #######
    objeto_apagarPostesteModel = PostesteModel.objetos.using(banquinho).all()
    for item in objeto_apagarPostesteModel:
        item.Alternativa_A_escolhida = ''
        item.Alternativa_B_escolhida = ''
        item.Alternativa_C_escolhida = ''
        item.Alternativa_D_escolhida = ''
        item.Alternativa_E_escolhida = ''
        item.Escolheu = ''
        item.save()

    ##### RESETANDO PROCEDIMENTOMODEL #######
    objeto_apagarProcedimentoModel = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_apagarProcedimentoModel.SessaoAtual= '1'
    objeto_apagarProcedimentoModel.ModuloAtual = '1'
    objeto_apagarProcedimentoModel.ModuloAntigo = '1'
    objeto_apagarProcedimentoModel.Retreino = '0'
    objeto_apagarProcedimentoModel.AgoraTreino = '0'

    objeto_apagarProcedimentoModel.EtapaAtual = 'pré-teste'

    """
    objeto_apagarProcedimentoModel.Etapa01 = '1'
    objeto_apagarProcedimentoModel.Etapa02 = '1'
    objeto_apagarProcedimentoModel.Etapa03 = '1'
    objeto_apagarProcedimentoModel.Etapa04 = '1'
    objeto_apagarProcedimentoModel.Etapa05 = '1'
    objeto_apagarProcedimentoModel.Etapa06 = '1'
    objeto_apagarProcedimentoModel.Etapa07 = '1'
    objeto_apagarProcedimentoModel.Etapa08 = '1'
    objeto_apagarProcedimentoModel.Etapa09 = '1'
    objeto_apagarProcedimentoModel.Etapa10 = '1'
    objeto_apagarProcedimentoModel.Etapa11 = '1'
    objeto_apagarProcedimentoModel.Etapa12 = '1'
    objeto_apagarProcedimentoModel.Etapa13 = '1'
    objeto_apagarProcedimentoModel.Etapa14 = '1'
    objeto_apagarProcedimentoModel.Etapa15 = '1'
    objeto_apagarProcedimentoModel.Etapa16 = '1'
    objeto_apagarProcedimentoModel.Etapa17 = '1'
    objeto_apagarProcedimentoModel.Etapa18 = '1'
    objeto_apagarProcedimentoModel.Etapa19 = '1'
    objeto_apagarProcedimentoModel.Etapa20 = '1'

    objeto_apagarProcedimentoModel.Acesso01_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso01_treino = '1'
    objeto_apagarProcedimentoModel.Acesso02_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso02_treino = '1'
    objeto_apagarProcedimentoModel.Acesso03_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso03_treino = '1'
    objeto_apagarProcedimentoModel.Acesso04_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso04_treino = '1'
    objeto_apagarProcedimentoModel.Acesso05_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso05_treino = '1'
    objeto_apagarProcedimentoModel.Acesso06_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso06_treino = '1'
    objeto_apagarProcedimentoModel.Acesso07_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso07_treino = '1'
    objeto_apagarProcedimentoModel.Acesso08_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso08_treino = '1'
    objeto_apagarProcedimentoModel.Acesso09_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso09_treino = '1'
    objeto_apagarProcedimentoModel.Acesso10_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso10_treino = '1'
    objeto_apagarProcedimentoModel.Acesso11_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso11_treino = '1'
    objeto_apagarProcedimentoModel.Acesso12_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso12_treino = '1'
    objeto_apagarProcedimentoModel.Acesso13_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso13_treino = '1'
    objeto_apagarProcedimentoModel.Acesso14_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso14_treino = '1'
    objeto_apagarProcedimentoModel.Acesso15_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso15_treino = '1'
    objeto_apagarProcedimentoModel.Acesso16_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso16_treino = '1'
    objeto_apagarProcedimentoModel.Acesso17_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso17_treino = '1'
    objeto_apagarProcedimentoModel.Acesso18_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso18_treino = '1'
    objeto_apagarProcedimentoModel.Acesso19_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso19_treino = '1'
    objeto_apagarProcedimentoModel.Acesso20_preteste = '1'
    objeto_apagarProcedimentoModel.Acesso20_treino = '1'

    objeto_apagarProcedimentoModel.Acesso01_posteste = '0'
    objeto_apagarProcedimentoModel.Acesso02_posteste = '0'
    objeto_apagarProcedimentoModel.Acesso03_posteste = '0'
    """

    objeto_apagarProcedimentoModel.save()

    ##### RESETANDO SESSAOMODEL #######
    SessaoModel.objetos.using(banquinho).all().delete()
    SessaoModel.objetos.using(banquinho).get_or_create(pk='1')


    ##### RESETANDO PRETESTEMODEL #######

    ##### RESETANDO ModulosModel #######
    objeto_apagarModulosModel = ModulosModel.objetos.using(banquinho).all()
    for item in objeto_apagarModulosModel:
        item.Modulo_EtapaAtual = '1'
        item.save()

    SeApagou = 'Reset Ok'
    if SeApagou == 'Reset Ok':
        return redirect('url_Entrada_configuracoes')

    context = {
        'resultado': SeApagou
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

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
        item.Acertou= '0'
        item.Jafoi = '0'
        item.Corretas = '0'
        item.Porcentagem = '0'
        item.save()

    SeApagou = 'EprogModel OK. Registros resetados'
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
    objeto_apagar.save()

    SeApagou = 'CalculosModel OK. Registros resetados'
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

    SeApagou = 'ProcedimeentoModel OK. Registros resetados'
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
    SeApagou = 'SessaoModel OK. Registros resetados'
    context = {
        'resultado': SeApagou
    }
    return render(request, "EprogApp/Entrada_configuracoes.html", context)

@staff_member_required
def Entrada_relatorios(request):
    user = request.user
    banquinho = str(user)

    if request.POST.get('treino'):
        listax= SessaoModel.objetos.using(banquinho).values_list(
            'Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent', )

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="Eprog_treino.csv"'
        writer = csv.writer(response)
        writer.writerow(['Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent'])
        for item in listax:
            print(item)
            writer = csv.writer(response)
            writer.writerow([item])
        return response

    if request.POST.get('preteste'):
        listax = PretesteModel.objetos.using(banquinho).values_list(
            'Participante',
            'Ordem', 'Modulo',
            #'Questao',
            #'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E',
            'Alternativa_A_escolhida', 'Alternativa_B_escolhida', 'Alternativa_C_escolhida',
            'Alternativa_D_escolhida', 'Alternativa_E_escolhida')

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="Eprog_preteste.csv"'
        writer = csv.writer(response)
        writer.writerow(['Participante',
                         'Ordem', 'Modulo',
                         #'Questao',
                         #'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E',
                         'Alternativa_A_escolhida', 'Alternativa_B_escolhida', 'Alternativa_C_escolhida',
                         'Alternativa_D_escolhida', 'Alternativa_E_escolhida'])
        for item in listax:

            print(item)
            writer = csv.writer(response)
            writer.writerow([item])
        return response

    if request.POST.get('posteste'):
        listax = PretesteModel.objetos.using(banquinho).values_list(
            'Participante',
            'Ordem', 'Modulo',
            #'Questao',
            #'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E',
            'Alternativa_A_escolhida', 'Alternativa_B_escolhida', 'Alternativa_C_escolhida',
            'Alternativa_D_escolhida', 'Alternativa_E_escolhida')

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="Eprog_posteste.csv"'
        writer = csv.writer(response)
        writer.writerow(['Participante',
                         'Ordem', 'Modulo',
                          #'Questao',
                          #'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E',
                         'Alternativa_A_escolhida', 'Alternativa_B_escolhida', 'Alternativa_C_escolhida',
                         'Alternativa_D_escolhida', 'Alternativa_E_escolhida'])
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
    n_tentativa = objetinho_sessao.Topico
    objetinho = EprogModel.objetos.using(banquinho).get(pk=n_tentativa)
    form = EprogForm(request.POST or None, instance=objetinho)
    objeto_procedimento = ProcedimentoModel.objetos.get(pk=1)
    obj = EprogModel.objetos.using(banquinho).last()
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    n_tentativa = objetinho_sessao.Topico
    objetinho = EprogModel.objetos.using('banquinho').get(pk=n_tentativa)
    form = EprogForm(request.POST or None, instance=objetinho)

    """
    if 1 + 1 == 2:
        context = {
            'objetinho_sessao': objetinho_sessao,
            "form": form,
            "objetinho": objetinho}
        return redirect('url_principal', pk= n_tentativa)
    """

    context = {
        "objetinho_sessao": objetinho_sessao,
        "form": form,
        "objetinho": objetinho,
        "n_tentativa": n_tentativa
    }
    return render(request, "EprogApp/comecar_sessao.html", context)

#@login_required
def update(request, pk):
    data = {}
    objetinho = EprogModel.objetos.get(pk=pk)
    objetinho2 = CalculosModel.objetos.get(pk=1)
    objetinho_ordem = CalculosModel.objetos.get(pk=1)
    objetinho_sessao = SessaoModel.objetos.get(pk=1)
    #n_tentativa = objetinho_sessao.Topico

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
        Topico_next = objetinho_sessao_atual.Topico
        #ordem_atual = objetinho_sessao_atual.Ordem
        #ordem_atual += 1
        #objetinho_sessao_next = SessaoModel.objeto_sessao.get(pk=ordem_atual)

        context = {
            "form": form,
            "objetinho": objetinho,
            #"objetinho2": objetinho2,
            "objetinho_sessao": objetinho_sessao_atual,
            "n_tentativa": Topico_next
            }
        #return render("EprogApp/principal.html", context)
        return redirect('url_update', pk= Topico_next)


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
        objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
        objeto_calculo = CalculosModel.objetos.using(banquinho).get(pk=1)

        n_modulo = objeto_procedimento.ModuloAtual
        objeto_modulos = ModulosModel.objetos.using(banquinho).get(pk=n_modulo)
        todas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= n_modulo).count()
        todas_ativadas = EprogModel.objetos.using(banquinho).filter(Ativada='1', Modulo= n_modulo).count()
        print("todas módulo: ", todas_modulo, "todas ativadas: ", todas_ativadas)

        quantas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= n_modulo, Ativada='1').count()
        corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= n_modulo).filter(Acertou='1').count()
        porcento_modulo = int((corretas_modulo/quantas_modulo)*100)
        objeto_calculo.TotalModulo= quantas_modulo
        objeto_calculo.Porcentagem= porcento_modulo
        objeto_calculo.Corretas= corretas_modulo
        objeto_calculo.save()
        #corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= '3' and Acertou='1').count()

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
            qualmodulo = objeto_procedimento.ModuloAtual
            modulo_sorteado = obj_sorteio.Modulo
            x_ativada = obj_sorteio.Ativada

            while SeAcertou == '1' or qualmodulo != modulo_sorteado or x_ativada == '0':
                n_rand = randint(1, total)
                obj_sorteio = EprogModel.objetos.using(banquinho).get(pk=n_rand)
                SeAcertou = obj_sorteio.Acertou
                modulo_sorteado = obj_sorteio.Modulo
                x_ativada = obj_sorteio.Ativada
            return redirect('url_sessao_testar', pk=n_rand)

        if request.POST.get('Sessao'):
            return redirect('url_sessao', pk=pk)

        if request.POST.get('Resposta'):
            return redirect('url_sessao', pk=pk)

        if request.POST.get('Sair'):
            return redirect('url_Entrada_Iniciar')
            # fazer o logout aqui:
            # return redirect('logout')

        if request.POST.get('Upload'):
            # fazer o logout aqui:
            print('Nada... Está desativado')
            #return redirect('url_sessao_upload', pk=pk)

        if request.POST.get('Correta'):
            Objeto_Procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
            objeto_calculo = CalculosModel.objetos.using(banquinho).get(pk=1)
            obj_linhaum = EprogModel.objetos.using(banquinho).get(pk=1)
            objeto_sessaoUm = SessaoModel.objetos.using(banquinho).get(pk=1)
            objeto_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
            objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)

            # Bloco 1 - início
            objetinho.SuaResposta= ''
            objetinho.save()
            objetinho.Acertou = '1'
            objetinho.Jafoi = '1'
            objetinho.save()

            corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo=n_modulo).filter(Acertou='1').count()
            porcento_modulo = int((corretas_modulo / quantas_modulo) * 100)
            objeto_calculo.TotalModulo = quantas_modulo
            objeto_calculo.Porcentagem = porcento_modulo
            objeto_calculo.Corretas = corretas_modulo
            objeto_calculo.save()
            porcento = objeto_calculo.Porcentagem

            tcorretas = EprogModel.objetos.using(banquinho).filter(Acertou='1').count()
            obj_linhaum.Corretas = str(tcorretas)
            obj_linhaum.Porcentagem = str(porcento_modulo)
            obj_linhaum.save()

            campo = 'id'
            obj_ult = EprogModel.objetos.using(banquinho).last()
            total_rec = getattr(obj_ult, campo)
            tporcentagem = (tcorretas/total_rec)*100
            if objetinho.id == 1:
                obj_linhaum.Acertou = '1'
                obj_linhaum.save()
            obj_linhaum.save()

            # fim do procedimento
            if porcento == 100.0:
                objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
                obj_linhaum = EprogModel.objetos.using(banquinho).get(pk=1)
                objeto_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)

                objeto_sessaoUm = SessaoModel.objetos.using(banquinho).get(pk=1)
                objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
                objeto_eprog_tudo = ProcedimentoModel.objetos.using(banquinho).all()
                objeto_calculo = CalculosModel.objetos.using(banquinho).get(pk=1)

                n_modulo = objeto_procedimento.ModuloAtual
                quantas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo=n_modulo).count()
                corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo=n_modulo).filter(Acertou='1').count()
                porcent_modulo = int((corretas_modulo / quantas_modulo) * 100)
                objeto_calculo.TotalModulo = quantas_modulo
                objeto_calculo.Porcentagem = porcent_modulo
                objeto_calculo.Corretas = corretas_modulo
                objeto_calculo.save()

                # Populando o arquivo de saída início
                if Objeto_Procedimento.Botao_avalia == '0':
                    x_ModuloAntigo = objeto_procedimento.ModuloAntigo
                    quantos_saida = SessaoModel.objetos.using(banquinho).count()
                    pk_next = quantos_saida + 1
                    objeto_saida = SessaoModel.objetos.using(banquinho).last()
                    objeto_saida.pk = None
                    objeto_saida.pk = pk_next
                    objeto_saida.id = pk_next
                    objeto_saida.save()
                    objeto_sessao = SessaoModel.objetos.using(banquinho).last()
                    pk_ultimo = objeto_sessao.pk
                    objeto_sessao.Dia = str(datetime.date.today())
                    objeto_sessao.Horario = datetime.datetime.now().strftime('%H:%M:%S')
                    objeto_sessao.Tentativa = pk_ultimo
                    objeto_sessao.Ordem = objetinho.Ordem
                    objeto_sessao.Topico = objetinho.Topico
                    objeto_sessao.DuvidaComent = objetinho.DuvidaComent
                    objeto_sessao.Sessao = Objeto_Procedimento.SessaoAtual
                    objeto_sessao.Acertou = objetinho.Acertou
                    objeto_sessao.Modulo = x_ModuloAntigo
                    objeto_sessao.save()
                    objetinho.Jafoi = '1'  ## mudou de lugar
                    objetinho.save()
                    Objeto_Procedimento.Botao_avalia = '1'
                    Objeto_Procedimento.save()
                    # Populando o arquivo de saída - fim

                if objeto_procedimento.Retreino == '1':
                    x_retreino = objeto_procedimento.Retreino
                    print('retreino é: ', x_retreino)
                    objeto_eprog_tudo = ProcedimentoModel.objetos.using(banquinho).all()
                    objeto_calculo = CalculosModel.objetos.using(banquinho).get(pk=1)
                    objeto_calculo.Porcentagem = '0'
                    objeto_calculo.Corretas = '0'
                    objeto_calculo.save()

                    objeto_apagarEprogModel = EprogModel.objetos.using(banquinho).all()
                    for item in objeto_apagarEprogModel:
                        item.DuvidaComent = ''
                        item.Marcador1 = ''
                        item.Marcador2 = ''
                        item.Marcador3 = ''
                        item.Marcador4 = ''
                        item.Marcador5 = ''
                        item.Acertou = '0'
                        item.Jafoi = '0'
                        item.Corretas = '0'
                        item.Porcentagem = '0'
                        item.save()

                    objeto_procedimento.ModuloAtual = objeto_procedimento.ModuloAntigo
                    objeto_procedimento.Retreino = '0'
                    objeto_procedimento.save()
                    return render(request, "EprogApp/sessao_fim_modulo.html")

                if objeto_procedimento.Retreino == '0':
                    num_modulo = int(n_modulo)
                    objeto_procedimento.AgoraTreino = '0'
                    x_TemPosTeste = objeto_modulos.TemPosTeste


                    if x_TemPosTeste == 1:
                        objeto_modulos.Modulo_EtapaAtual = '3'
                        objeto_procedimento.EtapaAtual = 'Pós-teste'
                        objeto_modulos.save()
                        objeto_procedimento.save()
                    else:
                        num_modulo_atualizado = num_modulo + 1
                        x_modulo_atualizado = str(num_modulo_atualizado)
                        objeto_procedimento.ModuloAtual = x_modulo_atualizado
                        objeto_procedimento.ModuloAntigo = x_modulo_atualizado
                        objeto_modulos.Modulo_EtapaAtual = '1'
                        objeto_procedimento.EtapaAtual = 'Pré-teste'
                        objeto_modulos.save()
                        objeto_procedimento.save()

                    return redirect('url_sessao_fim_modulo', pk=1)

                for item in objeto_eprog_tudo:
                        item.Acertou = '0'
                        item.Jafoi = '0'
                        item.save()

                context = {
                    "form": form,
                    "objetinho": objetinho,
                    "obj_linhaum": obj_linhaum,
                    "objetinhoSessao": objeto_sessao,
                    "objeto_sessaoUm": objeto_sessaoUm
                }
                return render(request, "EprogApp/sessao_fim_modulo.html", context)

            # Bloco 1- fim

            #Populando o arquivo de saída início
            if Objeto_Procedimento.Botao_avalia == '0':
                x_ModuloAntigo = objeto_procedimento.ModuloAntigo
                quantos_saida = SessaoModel.objetos.using(banquinho).count()
                pk_next = quantos_saida + 1
                objeto_saida = SessaoModel.objetos.using(banquinho).last()
                objeto_saida.pk = None
                objeto_saida.pk = pk_next
                objeto_saida.id = pk_next
                objeto_saida.save()
                objeto_sessao = SessaoModel.objetos.using(banquinho).last()
                pk_ultimo= objeto_sessao.pk
                objeto_sessao.Dia = str(datetime.date.today())
                objeto_sessao.Horario = datetime.datetime.now().strftime('%H:%M:%S')
                objeto_sessao.Tentativa = pk_ultimo
                objeto_sessao.Ordem = objetinho.Ordem
                objeto_sessao.Topico = objetinho.Topico
                objeto_sessao.Participante = objeto_procedimento.Participante
                objeto_sessao.DuvidaComent = objetinho.DuvidaComent
                objeto_sessao.Sessao = Objeto_Procedimento.SessaoAtual
                objeto_sessao.Acertou = objetinho.Acertou
                objeto_sessao.Modulo = x_ModuloAntigo
                objeto_sessao.save()
                objetinho.Jafoi = '1' ## mudou de lugar
                objetinho.save()
                Objeto_Procedimento.Botao_avalia = '1'
                Objeto_Procedimento.save()
                # Populando o arquivo de saída - fim

            if tcorretas == total_rec:
                return redirect('url_parabens_view')

            context = {
                "form": form,
                "objetinho": objetinho,
                "obj_linhaum": obj_linhaum,
                # "objetinho2": objetinho2,
                "objetinhoSessao": objeto_sessao,
                "objeto_sessaoUm": objeto_sessaoUm,
                "objeto_calculo": objeto_calculo,
                "objeto_procedimento": objeto_procedimento,

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
            tporcentagem = int((tcorretas / total_rec) * 100)
            obj_linhaum.Porcentagem = str(tporcentagem)
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
                objeto_sessao.Participante = objetinho.Participante
                objeto_sessao.Sessao = Objeto_Procedimento.SessaoAtual
                objeto_sessao.Acertou = objetinho.Acertou
                objeto_sessao.save()
                objetinho.Jafoi = '1'  ## mudou de lugar
                objetinho.save()
                Objeto_Procedimento.Botao_avalia = '1'
                Objeto_Procedimento.save()
                # Populando o arquivo de saída - fim

            context = {
                "form": form,
                "objetinho": objetinho,
                "obj_linhaum": obj_linhaum,
                # "objetinho2": objetinho2,
                "objetinhoSessao": objeto_sessao,
                "objeto_sessaoUm": objeto_sessaoUm,
                "objeto_calculo": objeto_calculo,
                "objeto_procedimento": objeto_procedimento,
            }
            return render(request, "EprogApp/sessao.html", context)

        context = {
            "form": form,
            "objetinho": objetinho,
            "obj_linhaum": obj_linhaum,
            # "objetinho2": objetinho2,
            "objeto_sessao": objeto_sessao,
            "objeto_sessaoUm": objeto_sessaoUm,
            "objeto_procedimento": objeto_procedimento,
            "objeto_calculo": objeto_calculo,
            "porcento_modulo": porcento_modulo,
            }
        return render(request, "EprogApp/sessao.html", context)

#@login_required
def sessao_fim_modulo_view(request, pk):
        user = request.user
        banquinho = str(user)
        objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
         #corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= '3' and Acertou='1').count()
        form = EprogForm(request.POST or None, instance=objetinho)

        if request.POST.get('Sair'):
            return redirect('url_Entrada_Iniciar')
            # fazer o logout aqui:
            # return redirect('logout')

              #form = EprogForm(request.POST or None, instance=objetinho)
            #if form.is_valid():
            #    form.save()

        context = {
            "form": form,
            "objetinho": objetinho,
            # "obj_linhaum": obj_linhaum,
            # "objetinho2": objetinho2,
            # "objeto_sessao": objeto_sessao,
            # "objeto_sessaoUm": objeto_sessaoUm,
            # "objeto_procedimento": objeto_procedimento,
            # "objeto_calculo": objeto_calculo,
            }
        return render(request, "EprogApp/sessao_fim_modulo.html", context)

"""
#@login_required
def preteste_view(request, pk):
        user = request.user
        banquinho = str(user)

        objeto_PretesteModel = PretesteModel.objetos.using(banquinho).get(pk=pk)
        form = PretesteForm(request.POST or None, instance=objeto_PretesteModel)

        if request.POST.get('Sair'):
            return redirect('url_Entrada_Iniciar')

        if request.POST.get('Confirmar'):
            alternativa_escolhida = ''
            print('alternativa escolhida foi: ', alternativa_escolhida)

            return redirect('url_Entrada_sobre')

        listao_preteste= PretesteModel.objetos.using(banquinho).values_list('Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E')
        for item in listao_preteste:
            print(item)

        context = {
            "form": form,
            "objeto_PretesteModel": objeto_PretesteModel,
            "listao_preteste": listao_preteste
            }
        return render(request, "EprogApp/Preteste.html", context)
"""

#@login_required
def preteste_view2(request, pk):
        user = request.user
        banquinho = str(user)

        Objeto_ProcedimentoModel = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
        X_modulo_atual = Objeto_ProcedimentoModel.ModuloAntigo
        n_modulo_atual = int(X_modulo_atual)
        objeto_modulos = ModulosModel.objetos.using(banquinho).get(pk=n_modulo_atual)
        n_PreTeste_Primeiro = objeto_modulos.PreTeste_Primeiro
        n_PreTeste_Ultimo = objeto_modulos.PreTeste_Ultimo

        objeto_PretesteModel = PretesteModel.objetos.using(banquinho).get(pk=pk)
        objeto_PretesteModel_linhaum = PretesteModel.objetos.using(banquinho).get(pk=1)
        x_modulo_preteste = objeto_PretesteModel.Modulo
        form = PretesteForm_executar(request.POST or None, instance=objeto_PretesteModel)

        x_Alternativa_A_escolhida = objeto_PretesteModel.Alternativa_A_escolhida
        x_Alternativa_B_escolhida = objeto_PretesteModel.Alternativa_B_escolhida
        x_Alternativa_C_escolhida = objeto_PretesteModel.Alternativa_C_escolhida
        x_Alternativa_D_escolhida = objeto_PretesteModel.Alternativa_D_escolhida
        x_Alternativa_E_escolhida = objeto_PretesteModel.Alternativa_E_escolhida


        if request.POST.get('primeiro'):
            return redirect('url_Preteste2', pk=n_PreTeste_Primeiro)

        if request.POST.get('ultimo'):
            return redirect('url_Preteste2', pk=n_PreTeste_Ultimo)

        if request.POST.get('proximo'):
            campo = 'id'
            user = request.user
            banquinho = str(user)
            obj_ultimo = PretesteModel.objetos.using(banquinho).get(pk=n_PreTeste_Ultimo)
            valor_ultimo = getattr(obj_ultimo, campo)
            total = valor_ultimo
            obj_atual = PretesteModel.objetos.using(banquinho).get(pk=pk)
            valor_campo = getattr(obj_atual, campo)
            n = valor_campo + 1
            if n > total:
                n = n_PreTeste_Primeiro
            return redirect('url_Preteste2', pk=n)

        if request.POST.get('anterior'):
            campo = 'id'
            obj = PretesteModel.objetos.using(banquinho).get(pk=pk)
            valor_campo = getattr(obj, campo)
            n = valor_campo - 1
            if n <= n_PreTeste_Primeiro:
                n = n_PreTeste_Primeiro
            return redirect('url_Preteste2', pk=n)

        if request.POST.get('Sair'):
            return redirect('url_Entrada_Iniciar')

        if request.POST.get('Finalizar_preteste'):
            x_participante = Objeto_ProcedimentoModel.Participante
            objeto_PretesteModel_linhaum.Participante = x_participante
            objeto_PretesteModel_linhaum.save()
            x_participante = objeto_PretesteModel_linhaum.Participante
            n_modulo = Objeto_ProcedimentoModel.ModuloAtual
            objeto_modulos = ModulosModel.objetos.using(banquinho).get(pk=n_modulo)
            x_Delineamento = objeto_modulos.Delineamento
            x_TemPosTeste = objeto_modulos.TemPosTeste

            if x_Delineamento == 'e':
                Objeto_ProcedimentoModel.AgoraTreino = '1'
                Objeto_ProcedimentoModel.save()
                x_moduloatual = Objeto_ProcedimentoModel.ModuloAntigo
                objeto_modulos.Modulo_EtapaAtual = '2'
                Objeto_ProcedimentoModel.EtapaAtual = 'Treino'
                objeto_modulos.save()
                Objeto_ProcedimentoModel.save()
                return redirect('url_Entrada_Iniciar')

            if x_Delineamento == 'c' and x_TemPosTeste == 0: # vai para o próximo modulo para fazer pré-teste
                Objeto_ProcedimentoModel.AgoraTreino = '0'
                n_modulo = Objeto_ProcedimentoModel.ModuloAtual
                num_modulo = int(n_modulo)
                num_modulo_atualizado = num_modulo + 1
                x_modulo_atualizado = str(num_modulo_atualizado)
                Objeto_ProcedimentoModel.ModuloAtual = x_modulo_atualizado
                Objeto_ProcedimentoModel.ModuloAntigo = x_modulo_atualizado
                Objeto_ProcedimentoModel.EtapaAtual = 'Pré-teste'
                objeto_modulos.save()
                Objeto_ProcedimentoModel.save()
                return redirect('url_Entrada_Iniciar')

            if x_Delineamento == 'c' and x_TemPosTeste == 1:  # vai para o pós-teste e faz se estiver disponível
                Objeto_ProcedimentoModel.AgoraTreino = '0'
                objeto_modulos.Modulo_EtapaAtual = '3'
                Objeto_ProcedimentoModel.EtapaAtual = 'Pós_Teste'
                objeto_modulos.save()
                Objeto_ProcedimentoModel.save()
                return redirect('url_Entrada_Iniciar')

        if request.POST.get('Confirmar'):
            alternativas = ''
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    alternativas = request.POST.getlist('alternativas')
                if alternativas == ['a']:
                    objeto_PretesteModel.Alternativa_A_escolhida = '1'
                    objeto_PretesteModel.Alternativa_B_escolhida = '0'
                    objeto_PretesteModel.Alternativa_C_escolhida = '0'
                    objeto_PretesteModel.Alternativa_D_escolhida = '0'
                    objeto_PretesteModel.Alternativa_E_escolhida = '0'
                    objeto_PretesteModel.save()

                if alternativas == ['b']:
                    objeto_PretesteModel.Alternativa_A_escolhida = '0'
                    objeto_PretesteModel.Alternativa_B_escolhida = '1'
                    objeto_PretesteModel.Alternativa_C_escolhida = '0'
                    objeto_PretesteModel.Alternativa_D_escolhida = '0'
                    objeto_PretesteModel.Alternativa_E_escolhida = '0'
                    objeto_PretesteModel.save()

                if alternativas == ['c']:
                    objeto_PretesteModel.Alternativa_A_escolhida = '0'
                    objeto_PretesteModel.Alternativa_B_escolhida = '0'
                    objeto_PretesteModel.Alternativa_C_escolhida = '1'
                    objeto_PretesteModel.Alternativa_D_escolhida = '0'
                    objeto_PretesteModel.Alternativa_E_escolhida = '0'
                    objeto_PretesteModel.save()

                if alternativas == ['d']:
                    objeto_PretesteModel.Alternativa_A_escolhida = '0'
                    objeto_PretesteModel.Alternativa_B_escolhida = '0'
                    objeto_PretesteModel.Alternativa_C_escolhida = '0'
                    objeto_PretesteModel.Alternativa_D_escolhida = '1'
                    objeto_PretesteModel.Alternativa_E_escolhida = '0'
                    objeto_PretesteModel.save()

                if alternativas == ['e']:
                    objeto_PretesteModel.Alternativa_A_escolhida = '0'
                    objeto_PretesteModel.Alternativa_B_escolhida = '0'
                    objeto_PretesteModel.Alternativa_C_escolhida = '0'
                    objeto_PretesteModel.Alternativa_D_escolhida = '0'
                    objeto_PretesteModel.Alternativa_E_escolhida = '1'
                    objeto_PretesteModel.save()

                context = {
                        "form": form,
                        "objeto_PretesteModel": objeto_PretesteModel,
                        "x_Alternativa_A_escolhida": x_Alternativa_A_escolhida,
                        "x_Alternativa_B_escolhida": x_Alternativa_B_escolhida,
                        "x_Alternativa_C_escolhida": x_Alternativa_C_escolhida,
                        "x_Alternativa_D_escolhida": x_Alternativa_D_escolhida,
                        "x_Alternativa_E_escolhida": x_Alternativa_E_escolhida
                }

                return redirect('url_Preteste2', pk=pk)

        context = {
            "form": form,
            "objeto_PretesteModel": objeto_PretesteModel,
            "x_Alternativa_A_escolhida": x_Alternativa_A_escolhida,
            "x_Alternativa_B_escolhida": x_Alternativa_B_escolhida,
            "x_Alternativa_C_escolhida": x_Alternativa_C_escolhida,
            "x_Alternativa_D_escolhida": x_Alternativa_D_escolhida,
            "x_Alternativa_E_escolhida": x_Alternativa_E_escolhida
            #"listao_preteste": listao_preteste
            }
        return render(request, "EprogApp/Preteste2.html", context)

#@login_required
def posteste_view(request, pk):
        user = request.user
        banquinho = str(user)

        objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
        X_modulo_atual = objeto_procedimento.ModuloAntigo
        x_modulo_final =objeto_procedimento.ModuloFinal

        Objeto_ProcedimentoModel = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
        n_modulo_atual = int(X_modulo_atual)
        objeto_modulos = ModulosModel.objetos.using(banquinho).get(pk=n_modulo_atual)
        n_PosTeste_Primeiro = objeto_modulos.PosTeste_Primeiro
        n_PosTeste_Ultimo = objeto_modulos.PosTeste_Ultimo

        #objeto_PostesteModel = PostesteModel.objetos.using(banquinho).get(pk=1)
        objeto_PostesteModel = PostesteModel.objetos.using(banquinho).get(pk=pk)
        x_modulo_posteste = objeto_PostesteModel.Modulo
        form = PostesteForm(request.POST or None, instance=objeto_PostesteModel)

        x_Alternativa_A_escolhida = objeto_PostesteModel.Alternativa_A_escolhida
        x_Alternativa_B_escolhida = objeto_PostesteModel.Alternativa_B_escolhida
        x_Alternativa_C_escolhida = objeto_PostesteModel.Alternativa_C_escolhida
        x_Alternativa_D_escolhida = objeto_PostesteModel.Alternativa_D_escolhida
        x_Alternativa_E_escolhida = objeto_PostesteModel.Alternativa_E_escolhida

        if request.POST.get('primeiro'):
            return redirect('url_Posteste', pk=n_PosTeste_Primeiro)

        if request.POST.get('ultimo'):
            return redirect('url_Posteste', pk=n_PosTeste_Ultimo)

        if request.POST.get('proximo'):
            campo = 'id'
            user = request.user
            banquinho = str(user)
            obj_ultimo = PostesteModel.objetos.using(banquinho).get(pk=n_PosTeste_Ultimo)
            valor_ultimo = getattr(obj_ultimo, campo)
            total = valor_ultimo
            obj_atual = PostesteModel.objetos.using(banquinho).get(pk=pk)
            valor_campo = getattr(obj_atual, campo)
            n = valor_campo + 1
            if n > total:
                n = n_PosTeste_Primeiro
            return redirect('url_Posteste', pk=n)

        if request.POST.get('anterior'):
            campo = 'id'
            obj = PostesteModel.objetos.using(banquinho).get(pk=pk)
            valor_campo = getattr(obj, campo)
            n = valor_campo - 1
            if n <= n_PosTeste_Primeiro:
                n = n_PosTeste_Primeiro
            return redirect('url_Posteste', pk=n)

        if request.POST.get('Sair'):
            return redirect('url_Entrada_Iniciar')

        if request.POST.get('Finalizar_posteste'):
            objeto_procedimento.AgoraTreino = '0'
            objeto_modulos.Modulo_EtapaAtual = '1'
            n_modulo = objeto_procedimento.ModuloAtual
            num_modulo = int(n_modulo)
            num_modulo_atualizado = num_modulo + 1
            x_modulo_atualizado = str(num_modulo_atualizado)
            objeto_procedimento.ModuloAtual = x_modulo_atualizado
            objeto_procedimento.ModuloAntigo = x_modulo_atualizado
            objeto_procedimento.EtapaAtual = 'Pré-teste'
            objeto_modulos.save()
            objeto_procedimento.save()

            # Estudo acabou
            if X_modulo_atual == x_modulo_final:
                return redirect('url_sessao_fim_modulo_final')

            return redirect('url_Entrada_Iniciar')

        if request.POST.get('Confirmar'):
            alternativas = ''
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    print('cheguei nas alternativas--')
                    alternativas = request.POST.getlist('alternativas')
                if alternativas == ['a']:
                    objeto_PostesteModel.Alternativa_A_escolhida = '1'
                    objeto_PostesteModel.Alternativa_B_escolhida = '0'
                    objeto_PostesteModel.Alternativa_C_escolhida = '0'
                    objeto_PostesteModel.Alternativa_D_escolhida = '0'
                    objeto_PostesteModel.Alternativa_E_escolhida = '0'
                    objeto_PostesteModel.save()
                    print('You selected a')

                if alternativas == ['b']:
                    objeto_PostesteModel.Alternativa_A_escolhida = '0'
                    objeto_PostesteModel.Alternativa_B_escolhida = '1'
                    objeto_PostesteModel.Alternativa_C_escolhida = '0'
                    objeto_PostesteModel.Alternativa_D_escolhida = '0'
                    objeto_PostesteModel.Alternativa_E_escolhida = '0'
                    objeto_PostesteModel.save()
                    print('You selected b')

                if alternativas == ['c']:
                    objeto_PostesteModel.Alternativa_A_escolhida = '0'
                    objeto_PostesteModel.Alternativa_B_escolhida = '0'
                    objeto_PostesteModel.Alternativa_C_escolhida = '1'
                    objeto_PostesteModel.Alternativa_D_escolhida = '0'
                    objeto_PostesteModel.Alternativa_E_escolhida = '0'
                    objeto_PostesteModel.save()
                    print('You selected c')

                if alternativas == ['d']:
                    objeto_PostesteModel.Alternativa_A_escolhida = '0'
                    objeto_PostesteModel.Alternativa_B_escolhida = '0'
                    objeto_PostesteModel.Alternativa_C_escolhida = '0'
                    objeto_PostesteModel.Alternativa_D_escolhida = '1'
                    objeto_PostesteModel.Alternativa_E_escolhida = '0'
                    objeto_PostesteModel.save()
                    print('You selected d')

                if alternativas == ['e']:
                    objeto_PostesteModel.Alternativa_A_escolhida = '0'
                    objeto_PostesteModel.Alternativa_B_escolhida = '0'
                    objeto_PostesteModel.Alternativa_C_escolhida = '0'
                    objeto_PostesteModel.Alternativa_D_escolhida = '0'
                    objeto_PostesteModel.Alternativa_E_escolhida = '1'
                    objeto_PostesteModel.save()
                    print('You selected e')

                context = {
                        "form": form,
                        "objeto_PostesteModel": objeto_PostesteModel,
                        "x_Alternativa_A_escolhida": x_Alternativa_A_escolhida,
                        "x_Alternativa_B_escolhida": x_Alternativa_B_escolhida,
                        "x_Alternativa_C_escolhida": x_Alternativa_C_escolhida,
                        "x_Alternativa_D_escolhida": x_Alternativa_D_escolhida,
                        "x_Alternativa_E_escolhida": x_Alternativa_E_escolhida
                }
                        # "listao_preteste": listao_preteste

                return redirect('url_Posteste', pk=pk)

        context = {
            "form": form,
            "objeto_PostesteModel": objeto_PostesteModel,
            "x_Alternativa_A_escolhida": x_Alternativa_A_escolhida,
            "x_Alternativa_B_escolhida": x_Alternativa_B_escolhida,
            "x_Alternativa_C_escolhida": x_Alternativa_C_escolhida,
            "x_Alternativa_D_escolhida": x_Alternativa_D_escolhida,
            "x_Alternativa_E_escolhida": x_Alternativa_E_escolhida
            #"listao_preteste": listao_preteste
            }
        return render(request, "EprogApp/Posteste.html", context)

#@login_required
def sessao_fim_modulo_final_view(request):
        user = request.user
        banquinho = str(user)
        objetinho = EprogModel.objetos.using(banquinho).get(pk=1)
         #corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= '3' and Acertou='1').count()
        form = EprogForm(request.POST or None, instance=objetinho)

        print('Se chegamos em sessao_fim_modulo_final_view--')

        if request.POST.get('Fim Mesmo'):
            print('aqui chegamos--')
            return redirect('url_Entrada_sobre')
            # fazer o logout aqui:
            # return redirect('logout')

              #form = EprogForm(request.POST or None, instance=objetinho)
            #if form.is_valid():
            #    form.save()

        if request.POST.get('Comecar_Posteste'):
            return redirect('url_Posteste', pk=1)

        context = {
            "form": form,
            "objetinho": objetinho,
            }
        return render(request, "EprogApp/sessao_fim_modulo_final.html", context)

#@login_required
def sessao_fim_estudo_view(request):
        user = request.user
        banquinho = str(user)
        objetinho = EprogModel.objetos.using(banquinho).get(pk=1)
         #corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo= '3' and Acertou='1').count()
        form = EprogForm(request.POST or None, instance=objetinho)

        if request.POST.get('Fim Mesmo'):
            print('aqui chegamos--')
            return redirect('url_entrada')
            # fazer o logout aqui:
            # return redirect('logout')

              #form = EprogForm(request.POST or None, instance=objetinho)
            #if form.is_valid():
            #    form.save()

        #Não temos mais isso
        if request.POST.get('Comecar_Posteste'):
            return redirect('url_Posteste', pk=1)

        context = {
            "form": form,
            "objetinho": objetinho,
            }
        return render(request, "EprogApp/sessao_fim_estudo.html")

@login_required
def sessao_testar(request, pk):
    user = request.user
    banquinho = str(user)
    # data = {}
    objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    objeto_procedimento.Botao_avalia = '0'
    objeto_procedimento.save()
    objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    objeto_calculo = CalculosModel.objetos.using(banquinho).get(pk=1)

    n_modulo = objeto_procedimento.ModuloAtual
    quantas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo=n_modulo, Ativada='1').count()
    corretas_modulo = EprogModel.objetos.using(banquinho).filter(Modulo=n_modulo).filter(Acertou='1').count()
    porcent_modulo = int((corretas_modulo / quantas_modulo) * 100)
    objeto_calculo.TotalModulo = quantas_modulo
    objeto_calculo.Porcentagem = porcent_modulo
    objeto_calculo.Corretas = corretas_modulo
    objeto_calculo.save()

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
        "objetinhoSessao": objetinhoSessao,
        "objeto_procedimento": objeto_procedimento,
        "objeto_calculo": objeto_calculo,
    }
    return render(request, "EprogApp/sessao_testar.html", context)

