class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self,valor):
        self.velocidade += valor

    def frear(self,frear):
        self.velocidade -= frear
    
    def status(self):
        print(f"modelo: {self.modelo}\nstatus: {self.velocidade}")
carro = Carro("Fiat")
carro.acelerar(200)
carro.frear(50)
carro.status()