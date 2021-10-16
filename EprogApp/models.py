from django.db import models

class EprogModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
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
    Porcentagem = models.IntegerField()
    Corretas= models.IntegerField()
    Incorretas = models.IntegerField()
    Ordem = models.IntegerField()

    objetos = models.Manager()

class ProcedimentoModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Banco =  models.TextField(max_length=500, blank=True, default='')
    NomeCompleto = models.CharField(max_length=200, blank=True, default='')
    Idade = models.TextField(max_length=3, blank=True, default='')
    Acesso = models.TextField(max_length=10, blank=True, default='')
    Botao_avalia = models.TextField(max_length=3, blank=True, default='0')
    SessaoAtual = models.TextField(max_length=3, blank=True, default='1')

    objetos = models.Manager()


class SessaoModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Modulo =        models.CharField(max_length=3, blank=True, default='1')
    Sessao =        models.CharField(max_length=3, blank=True, default='')
    Dia =           models.CharField(max_length=20, blank=True, default='')
    Horario =       models.CharField(max_length=20, blank=True, default='')
    Tentativa =     models.CharField(max_length=3, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Topico =        models.TextField(max_length=1000, blank=True, default='')
    DuvidaComent =  models.TextField(max_length=500, blank=True, default='')
    Acertou =       models.CharField(max_length=3, blank=True, default='0')

    objetos = models.Manager()