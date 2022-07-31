from django.db import models

class EprogModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Modulo=         models.CharField(max_length=3, blank=True, default='1')
    Numero=         models.CharField(max_length=3, blank=True, default=' ')
    Topico =        models.TextField(max_length=1000, blank=True, default='')
    Textao=         models.TextField(max_length=2000, blank=True, default='')
    SuaResposta =   models.TextField(max_length=2000, blank=True, default='')
    OndeFigura1 =   models.CharField(max_length=200, blank=True, default='')
    OndeFigura2 =   models.CharField(max_length=200, blank=True, default='')
    DuvidaComent =  models.TextField(max_length=500, blank=True, default='')
    Acertou =       models.CharField(max_length=3, blank=True, default='0')
    Jafoi =         models.CharField(max_length=3, blank=True, default='0')
    Ativada =       models.CharField(max_length=3, blank=True, default='1')
    Corretas =      models.CharField(max_length=3, blank=True, default='0')
    Porcentagem =   models.CharField(max_length=3, blank=True, default='0')
    Marcador1 =     models.TextField(max_length=300, blank=True, default='')
    Marcador2 =     models.TextField(max_length=300, blank=True, default='')
    Marcador3 =     models.TextField(max_length=300, blank=True, default='')
    Marcador4 =     models.TextField(max_length=300, blank=True, default='')
    Marcador5 =     models.TextField(max_length=300, blank=True, default='')
    title =         models.CharField(max_length=200, blank=True, default='')
    image =         models.ImageField(upload_to='images')

    #class Meta:
    #    order_with_respect_to = 'id'

    def __str__(self):
        return self.Topico

    #def __str__(self):
    #    return self.title

    objetos = models.Manager()

class CalculosModel(models.Model):
    id = models.AutoField(primary_key=True)
    TotalModulo= models.IntegerField(default=1)
    Porcentagem = models.IntegerField(default=0)
    Corretas= models.IntegerField(default=0)
    Incorretas = models.IntegerField()
    Ordem = models.IntegerField()
    Modulo=         models.CharField(max_length=3, blank=True, default='1')
    Numero=         models.CharField(max_length=3, blank=True, default=' ')
    objetos = models.Manager()

class ModulosModel(models.Model):
    id = models.AutoField(primary_key=True)
    Ordem = models.IntegerField()
    NoModulo = models.CharField(max_length=3, blank=True, default='')
    Descricao = models.CharField(max_length=200, blank=True, default='')
    Treino_Primeiro = models.IntegerField()
    Treino_Ultimo = models.IntegerField()
    PreTeste_Primeiro = models.IntegerField()
    PreTeste_Ultimo = models.IntegerField()
    TemPosTeste = models.IntegerField()
    PosTeste_Primeiro = models.IntegerField()
    PosTeste_Ultimo = models.IntegerField()
    Treino_Acesso = models.CharField(max_length=3, blank=True, default='1')
    PreTeste_Acesso = models.CharField(max_length=3, blank=True, default='1')
    PosTeste_Acesso = models.CharField(max_length=3, blank=True, default='1')
    Delineamento = models.CharField(max_length=3, blank=True, default='1') # 'c': controle
    Modulo_EtapaAtual = models.CharField(max_length=3, blank=True, default='1')
    # Para Modulo_EtapaAtual
    # 1 (não fez, pode fazer pré-treino)
    # 2 (fez pré-treino, pode fazer treino)
    # 3 (fez treino, pode fazer pós-teste)


    objetos = models.Manager()

class ProcedimentoModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Senha_Experimentador = models.CharField(max_length=200, blank=True, default='')
    Senha_Salva = models.CharField(max_length=200, blank=True, default='')
    Banco =  models.TextField(max_length=500, blank=True, default='')
    NomeCompleto = models.CharField(max_length=200, blank=True, default='')
    Idade = models.TextField(max_length=3, blank=True, default='')
    Acesso = models.TextField(max_length=10, blank=True, default='')
    Botao_avalia = models.TextField(max_length=3, blank=True, default='0')
    SessaoAtual = models.TextField(max_length=3, blank=True, default='1')
    ModuloAtual= models.CharField(max_length=3, blank=True, default='1')
    Condicao = models.CharField(max_length=3, blank=True, default='')

    # pré-teste, treino, pós-teste
    EtapaAtual= models.CharField(max_length=30, blank=True, default='pré-teste')
    ModuloAntigo= models.CharField(max_length=3, blank=True, default='1')
    ModuloFinal = models.TextField(max_length=3, blank=True, default='')
    AgoraTreino = models.TextField(max_length=3, blank=True, default='0')
    FimUltimoModulo = models.TextField(max_length=3, blank=True, default='0')
    FimEstudo = models.TextField(max_length=3, blank=True, default='0')
    Retreino = models.TextField(max_length=3, blank=True, default='0')

    # 0 (inacessível);
    # 1 (não fez, pode fazer pré-treino)
    # 2 (fez pré-treino, pode fazer treino)
    # 3 (fez treino, pode fazer pós-teste)
    # 4 (fez prós-teste, pode fazer pré-treino do próximo)

    objetos = models.Manager()


class SessaoModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Modulo =        models.CharField(max_length=3, blank=True, default='1')
    Numero=         models.CharField(max_length=3, blank=True, default=' ')
    Sessao =        models.CharField(max_length=3, blank=True, default='')
    Dia =           models.CharField(max_length=20, blank=True, default='')
    Horario =       models.CharField(max_length=20, blank=True, default='')
    Tentativa =     models.CharField(max_length=3, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Topico =        models.TextField(max_length=1000, blank=True, default='')
    DuvidaComent =  models.TextField(max_length=500, blank=True, default='')
    Acertou =       models.CharField(max_length=3, blank=True, default='0')

    objetos = models.Manager()

class PretesteModel(models.Model):
        id = models.AutoField(primary_key=True)
        Participante = models.CharField(max_length=200, blank=True, default='')
        Ordem = models.CharField(max_length=3, blank=True, default='')
        Modulo = models.CharField(max_length=3, blank=True, default='1')
        Acertou = models.CharField(max_length=3, blank=True, default='0')
        Jafoi = models.CharField(max_length=3, blank=True, default='0')
        Questao = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_A = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_B = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_C = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_D = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_E = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_X = models.CharField(max_length=2000, blank=True, default='')
        Alternativa_A_escolhida = models.CharField(max_length=3, blank=True, default='0')
        Alternativa_B_escolhida = models.CharField(max_length=3, blank=True, default='0')
        Alternativa_C_escolhida = models.CharField(max_length=3, blank=True, default='0')
        Alternativa_D_escolhida = models.CharField(max_length=3, blank=True, default='0')
        Alternativa_E_escolhida = models.CharField(max_length=3, blank=True, default='0')
        Escolheu = models.CharField(max_length=3, blank=True, default='')

        objetos = models.Manager()


class PostesteModel(models.Model):
    id = models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Modulo = models.CharField(max_length=3, blank=True, default='1')
    Numero_Posteste = models.CharField(max_length=3, blank=True, default='1')
    Posteste_Atual = models.CharField(max_length=3, blank=True, default='1')
    Acertou = models.CharField(max_length=3, blank=True, default='0')
    Jafoi = models.CharField(max_length=3, blank=True, default='0')
    Questao = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_A = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_B = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_C = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_D = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_E = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_X = models.CharField(max_length=2000, blank=True, default='')
    Alternativa_A_escolhida = models.CharField(max_length=3, blank=True, default='0')
    Alternativa_B_escolhida = models.CharField(max_length=3, blank=True, default='0')
    Alternativa_C_escolhida = models.CharField(max_length=3, blank=True, default='0')
    Alternativa_D_escolhida = models.CharField(max_length=3, blank=True, default='0')

    Alternativa_E_escolhida = models.CharField(max_length=3, blank=True, default='0')
    Escolheu = models.CharField(max_length=3, blank=True, default='')

    objetos = models.Manager()