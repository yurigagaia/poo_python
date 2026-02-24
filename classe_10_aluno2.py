import os
def limpar():
    os.system('cls')
limpar()
class Aluno():
    def __init__(self, nome, nota1, nota2):
        #atributos
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        #metodo
    def calcular_media(self):
        media = self.nota1 - self.nota1 / 2
        return media
    def mostrar_situacao(self):
        if self.calcular_media() > 7:
            return "aprovado"
        else:
            return "reprovado"
aluno1 = Aluno("yuri",10,8)
print(f"aluno: {aluno1.nome}")
print(f"situação: {aluno1.calcular_media()}")