import os
def limpar():
    os.system('cls')
limpar()
data_atual = 2026
class carro:
    def __init__(self,marca,data):
       self.marca = marca
       self.data = data
    def mostrar_tabela(self):
        print(f"o marca é {self.marca}")
        print(f"a data é {self.data}")
    def calcular_ano(self):
        ano = data_atual - self.data
        print(f"o ano é {ano}")
c1 = carro("fiat",2020)
c1.mostrar_tabela()
c1.calcular_ano()