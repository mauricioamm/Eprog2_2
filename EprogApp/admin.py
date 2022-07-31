from django.contrib import admin
from .models import EprogModel, CalculosModel, SessaoModel, ProcedimentoModel, PretesteModel

admin.site.register(EprogModel)
admin.site.register(CalculosModel)
admin.site.register(SessaoModel)
admin.site.register(ProcedimentoModel)
admin.site.register(PretesteModel)


