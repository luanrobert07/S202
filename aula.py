

from aluno import Aluno
from professor import Professor


class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        lista_alunos = ", ".join([aluno.nome for aluno in self.alunos])
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n{lista_alunos}"

professor1 = Professor("João")
aluno1 = Aluno("Lucas")
aluno2 = Aluno("Pedro")

aula1 = Aula(professor1, "Python")
aula1.adicionar_aluno(aluno1)
aula1.adicionar_aluno(aluno2)

print(aula1.listar_presenca())
