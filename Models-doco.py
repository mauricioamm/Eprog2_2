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

    #class Meta:
    #    order_with_respect_to = 'id'

    def __str__(self):
        return self.Topico

    objetos = models.Manager()
	
	