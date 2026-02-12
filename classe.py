import os
def limpar():
    os.system('cls')
limpar()
ano_atual = 2026
#criando uma classe
class carro:
#criando metodo construtor(é executado quando criamos o objeto)
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano
#metodo para mostrar os dados
    def mostrar_dados(self):
        print(f"a marca é {self.marca}")
        print(f"o modelo é {self.ano}")
    def calcular_ano(self):
        ano_atual
        ano =  ano_atual - self.ano
        print(f"o carro tem {ano} anos")
class moto:
    def __init__(self, marca,ano):
        self.marca = marca
        self.ano = ano
    def mostrar(self):
        print(f"a marca é {self.marca}")
        print(f"o ano é {self.ano}")
    def calcular_anom1(self):
        ano_atual
        moto =   ano_atual - self.ano
        print(f"a moto tem {moto} anos")
#criando objeto(uma pessoa)
c1 = carro("fiat",2024)
c1.calcular_ano()
m1 = moto("kawasaki",2000)

c1.mostrar_dados()
print("-" *40)
m1.calcular_anom1()
m1.mostrar()
