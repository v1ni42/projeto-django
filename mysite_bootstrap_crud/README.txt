Projeto Django CRUD com Bootstrap (mysite)

Como rodar (Windows - VSCode):

1) Crie e ative um virtualenv na pasta do projeto:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1    # PowerShell
   .\.venv\Scripts\activate.bat    # cmd

2) Instale dependências:
   pip install -r requirements.txt

3) (Opcional) Se quiser criar superuser:
   python manage.py createsuperuser

4) Rode o servidor:
   python manage.py runserver

5) Acesse:
   http://127.0.0.1:8000/       -> painel (links para Turmas, Professores, Alunos)
   http://127.0.0.1:8000/admin/ -> admin Django

Observações:
- O projeto já inclui um banco SQLite (db.sqlite3) com tabelas e alguns registros de exemplo.
- Se você usar este DB com migrations em um ambiente Django, poderá ver avisos de migrações pendentes; isso é normal porque incluí o DB manualmente.
