from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from EprogApp.views import principal_hidden, delete, criar, \
        teste_view, teste2_view, sessao_view, comecar_sessao_view, criar_tabela, clonar_model, \
        update, sessao_testar, parabens_view, entrada, sessao_fim_modulo_view, sessao_fim_modulo_final_view,\
        Entrada_Iniciar, Entrada_configuracoes, Entrada_relatorios, Entrada_sobre, Entrada_login,\
        teste_loop, \
        Editar_EprogModel, Editar_CalculosModel, Editar_ProcedimentoModel, Editar_SessaoModel,\
        Reset_Models,\
        Reset_EprogModel, Reset_CalculosModel, Reset_ProcedimentoModel, Reset_SessaoModel, \
        sessao_upload, Entrada_Iniciar_Normal, entrada_iniciar_retreino,  preteste_view2,\
        Entrada_Retreino_view, posteste_view, sessao_fim_estudo_view, Entrada_Iniciar_Indisponivel,\
        Editar_Preteste, Editar_Posteste,\
        Entrada_Experimentador_view, Editar_Modulos_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entrada, name='url_entrada'),
    path('criar/', criar, name= 'url_criar'),
    path('teste/', teste_view, name= 'url_teste_view'),
    path('teste2/', teste2_view, name= 'url_teste2_view'),
    path('preteste2/<int:pk>', preteste_view2, name='url_Preteste2'),
    path('posteste/<int:pk>', posteste_view, name='url_Posteste'),
    path('sessao_fim_estudo/', sessao_fim_estudo_view, name='url_sessao_fim_estudo'),


    path('teste_loop/', teste_loop, name= 'url_teste_loop_view'),
    path('criar_tabela/', criar_tabela, name= 'url_criar_tabela'),
    path('clonar/', clonar_model, name='url_clonar_model'),
    path('Parabens/', parabens_view, name='url_parabens_view'),
    path('Entrada_login/', Entrada_login, name='url_Entrada_login'),
    path('Entrada_Iniciar/', Entrada_Iniciar, name='url_Entrada_Iniciar'),
    path('Entrada_Retreino/', Entrada_Retreino_view, name='url_Entrada_Retreino'),
    path('Entrada_Experimentador/', Entrada_Experimentador_view, name='url_Entrada_Experimentador'),

    path('Entrada_Iniciar_Indisponivel/', Entrada_Iniciar_Indisponivel, name='url_Entrada_Iniciar_Indisponivel'),
    path('Entrada_Iniciar_Normal/', Entrada_Iniciar_Normal, name='url_Entrada_Iniciar_Normal'),
    path('Entrada_Iniciar_Retreino/', entrada_iniciar_retreino, name='url_Entrada_Iniciar_Retreino'),
    path('Entrada_configuracoes/', Entrada_configuracoes, name='url_Entrada_configuracoes'),
    path('Entrada_relatorios/', Entrada_relatorios, name='url_Entrada_relatorios'),
    path('Entrada_sobre/', Entrada_sobre, name='url_Entrada_sobre'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('update/<int:pk>/', update, name='url_update'),
    path('sessao/<int:pk>/', sessao_view, name='url_sessao'),
    path('sessao_fim_modulo/<int:pk>/', sessao_fim_modulo_view, name='url_sessao_fim_modulo'),
    path('sessao_fim_modulo_final/', sessao_fim_modulo_final_view, name='url_sessao_fim_modulo_final'),
    path('sessao_testar/<int:pk>/', sessao_testar, name='url_sessao_testar'),
    path('comecar_sessao/', comecar_sessao_view, name='url_comecar_sessao'),
    path('Editar_EprogModel/<int:pk>', Editar_EprogModel, name='url_Editar_EprogModel'),
    path('Editar_Preteste/<int:pk>', Editar_Preteste, name='url_Editar_Preteste'),
    path('Editar_Posteste/<int:pk>', Editar_Posteste, name='url_Editar_Posteste'),
    path('Editar_Modulos/<int:pk>', Editar_Modulos_view, name='url_Editar_Modulos'),



    path('Editar_CalculosModel/<int:pk>', Editar_CalculosModel, name='url_Editar_CalculosModel'),
    path('Editar_ProcedimentoModel/<int:pk>', Editar_ProcedimentoModel, name='url_Editar_ProcedimentoModel'),
    path('Editar_SessaoModel/<int:pk>', Editar_SessaoModel, name='url_Editar_SessaoModel'),

    path('Reset_EprogModel/', Reset_EprogModel, name='url_Reset_EprogModel'),
    path('Reset_CalculosModel/', Reset_CalculosModel, name='url_Reset_CalculosModel'),
    path('Reset_ProcedimentoModel/', Reset_ProcedimentoModel, name='url_Reset_ProcedimentoModel'),
    path('Reset_SessaoModel/<int:pk>', Reset_SessaoModel, name='url_Reset_SessaoModel'),
    path('Reset_Models/', Reset_Models, name='url_reset_models'),
    path('principal_hidden/<int:pk>/', principal_hidden, name='url_principal_hidden'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Sessao_Upload/<int:pk>/', sessao_upload, name='url_sessao_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)