from django.urls import path
from . import views

urlpatterns = [
    path("", views.TurmaList.as_view(), name="turma_list"),
    path("turma/add/", views.TurmaCreate.as_view(), name="turma_add"),
    path("turma/<int:pk>/edit/", views.TurmaUpdate.as_view(), name="turma_edit"),
    path("turma/<int:pk>/delete/", views.TurmaDelete.as_view(), name="turma_delete"),
    path("professores/", views.ProfessorList.as_view(), name="professor_list"),
    path("professores/add/", views.ProfessorCreate.as_view(), name="professor_add"),
    path("professores/<int:pk>/edit/", views.ProfessorUpdate.as_view(), name="professor_edit"),
    path("professores/<int:pk>/delete/", views.ProfessorDelete.as_view(), name="professor_delete"),
    path("alunos/", views.AlunoList.as_view(), name="aluno_list"),
    path("alunos/add/", views.AlunoCreate.as_view(), name="aluno_add"),
    path("alunos/<int:pk>/edit/", views.AlunoUpdate.as_view(), name="aluno_edit"),
    path("alunos/<int:pk>/delete/", views.AlunoDelete.as_view(), name="aluno_delete"),
]
