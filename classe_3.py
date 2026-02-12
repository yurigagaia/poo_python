import os
def limpar():
    os.system('cls')
limpar()
class item:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
        print(f"item: {self.nome}")
        print(f"preço: {self.preco:.2f}")
c1 = item("caderno",45.90)
c1.mostrar()