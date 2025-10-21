from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turma, Professor, Aluno
from .forms import TurmaForm, ProfessorForm, AlunoForm

class TurmaList(ListView):
    model = Turma
    template_name = "turma_list.html"

class TurmaCreate(CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = "turma_form.html"
    success_url = reverse_lazy('turma_list')
    
class TurmaUpdate(UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = "turma_form.html"
    success_url = reverse_lazy('turma_list')

class TurmaDelete(DeleteView):
    model = Turma
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('turma_list')

class ProfessorList(ListView):
    model = Professor
    template_name = "professor_list.html"

class ProfessorCreate(CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = "professor_form.html"
    success_url = reverse_lazy('professor_list')

class ProfessorUpdate(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = "professor_form.html"
    success_url = reverse_lazy('professor_list')

class ProfessorDelete(DeleteView):
    model = Professor
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('professor_list')

class AlunoList(ListView):
    model = Aluno
    template_name = "aluno_list.html"

class AlunoCreate(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "aluno_form.html"
    success_url = reverse_lazy('aluno_list')

class AlunoUpdate(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "aluno_form.html"
    success_url = reverse_lazy('aluno_list')
    
class AlunoDelete(DeleteView):
    model = Aluno
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('aluno_list')
