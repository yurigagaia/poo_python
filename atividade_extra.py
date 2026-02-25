import os
def limpar():
    os.system('cls')
limpar()

class Aluno():
    def __init__(self, nome, nota1, nota2):
    
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

    def mostrar_situacao(self):
        if self.calcular_media() >= 7:
            return "aprovado"
        else:
            return "reprovado"

aluno1 = Aluno("Yuri", 10, 8)
aluno2 = Aluno("Rafael", 10, 8)

print(f"aluno: {aluno1.nome}")
print(f"media: {aluno1.calcular_media()}")
print(f"{aluno1.mostrar_situacao()}")
print(f"media: {aluno2.calcular_media()}")
print(f"{aluno2.mostrar_situacao()}")

print("-" * 40)

class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def lecionar(self):
        print(f"professor: {self.nome} \nmateria: {self.disciplina}")

professor1 = Professor("frainy", "filosofia")
professor1.lecionar()

class Turma():
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"aluno: {aluno.nome}")
            print(f"media: {aluno.calcular_media()}")
            print(f"situacao: {aluno.mostrar_situacao()}")
            print("-" * 20)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.listar_alunos()


