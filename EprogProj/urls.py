from django.contrib import admin
from django.urls import path, include
from EprogApp.views import principal, principal_hidden, listagem, update, delete, criar, \
        teste_view, teste2_view, sessao_view, comecar_sessao_view, criar_tabela, clonar_model, \
        update, sessao_testar, parabens_view, entrada, \
        Entrada_Iniciar, Entrada_configuracoes, Entrada_relatorios, Entrada_sobre, Entrada_login,\
        teste_loop, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entrada, name='url_entrada'),
    #path('', listagem, name='url_listagem'),
    path('criar/', criar, name= 'url_criar'),
    path('teste/', teste_view, name= 'url_teste_view'),
    path('teste2/', teste2_view, name= 'url_teste2_view'),
    path('teste_loop/', teste_loop, name= 'url_teste_loop_view'),
    path('criar_tabela/', criar_tabela, name= 'url_criar_tabela'),
    path('clonar/', clonar_model, name='url_clonar_model'),
    path('Parabens/', parabens_view, name='url_parabens_view'),
    path('Entrada_login/', Entrada_login, name='url_Entrada_login'),
    path('Entrada_Iniciar/', Entrada_Iniciar, name='url_Entrada_Iniciar'),
    path('Entrada_configuracoes/', Entrada_configuracoes, name='url_Entrada_configuracoes'),
    path('Entrada_relatorios/', Entrada_relatorios, name='url_Entrada_relatorios'),
    path('Entrada_sobre/', Entrada_sobre, name='url_Entrada_sobre'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('principal/<int:pk>/', principal, name='url_principal'),
    path('update/<int:pk>/', update, name='url_update'),
    path('sessao/<int:pk>/', sessao_view, name='url_sessao'),
    path('sessao_testar/<int:pk>/', sessao_testar, name='url_sessao_testar'),
    path('comecar_sessao/', comecar_sessao_view , name='url_comecar_sessao'),
    path('principal_hidden/<int:pk>/', principal_hidden, name='url_principal_hidden'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),

]
