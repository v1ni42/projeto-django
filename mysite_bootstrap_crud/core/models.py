from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    numero = models.CharField(max_length=50, blank=True)
    disciplina = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.numero})" if self.numero else self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=200)
    documento = models.CharField(max_length=100, blank=True)
    disciplina = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    documento = models.CharField(max_length=100, blank=True)
    turma = models.CharField(max_length=200, blank=True, help_text="Texto livre — este projeto não usa FK")
    
    def __str__(self):
        return self.nome
