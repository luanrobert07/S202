class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f"O Aluno {self.nome} está presente."

aluno1 = Aluno("Lucas")
print(aluno1.presenca())