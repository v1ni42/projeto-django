from django import forms
from .models import Turma, Professor, Aluno

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome','numero','disciplina']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome','documento','disciplina']
        
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','documento','turma']
