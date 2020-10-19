def supesq_view(request):
    #objeto_bloco = Cond1Bloco01Model.objetos.get(pk=1)
    #objeto_saida = BlocoSaidaModel.objetos.get(pk=1) 
    objeto_saida_ultimo = BlocoSaidaModel.objetos.last()
    pk_ultimo = objeto_saida_ultimo.pk 
    objeto_bloco = Cond1Bloco01Model.objetos.last()
    objeto_saida = BlocoSaidaModel.objetos.last()    
    # objeto_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_saida.Escolheu = '1'
    objeto_saida.Acertou = '0'
    if objeto_bloco.Correta == objeto_saida.Escolheu:
        objeto_saida.Acertou = '1'        
        NCorretas = int(objeto_saida.Corretas)
        NCorretas += 1
        objeto_saida.Corretas = str(NCorretas)
        Porcent= int(NCorretas/pk_ultimo)        
        objeto_saida.Porcentagem = str(Porcent)        
    objeto_saida.save()
    return redirect('url_Jan_Modelo')