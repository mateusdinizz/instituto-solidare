from django.urls import path
from . import views

app_name = 'instsoli'

urlpatterns = [
    path('', views.home, name='home'),
    # cursos
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/<int:id>/', views.detalhe_curso, name='detalhe_curso'),
    path('cursos/criar/', views.criar_curso, name='criar_curso'),
    path('cursos/gerenciar_cursos/', views.gerenciar_cursos ,name="gerenciar_cursos"),
    path('cursos/excluir/<int:id>', views.excluir_curso, name='excluir_curso'),
    path('cursos/editar/<int:id>', views.editar_curso, name='editar_curso'),
    ## portal do professor
    path('portal_professor/', views.portal_professor, name='portal_professor'),
    # turmas 
    path('portal_professor/turmas/', views.gerenciar_turmas, name='gerenciar_turmas'),
    path('portal_professor/turmas/criar/', views.criar_turma, name='criar_turma'),
    path('portal_professor/turmas/excluir/<int:id>/', views.excluir_turma, name='excluir_turma'),
    path('portal_professor/turmas/editar/<int:id>/', views.editar_turma, name='editar_turma'),
    path('portal_professor/turmas/alunos/<int:id>/', views.ver_alunos, name='ver_alunos'),
    path('portal_professor/turmas/frequencia/<int:id>', views.registrar_frequencia, name='registrar_frequencia'),
]
