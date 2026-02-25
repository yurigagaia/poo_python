import os
def limpar():
    os.system('cls')
limpar()

class Jogo():
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
    def subir_nivel(self):
        self.nivel += 1
    def mostrar(self):
        print(f"nome: {self.nome} \nlevel: {self.nivel}")

jogador1 = Jogo("yurigagaia")
jogador1.subir_nivel()
jogador1.subir_nivel()
jogador1.mostrar()




