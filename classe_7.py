class Aparelhos:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
        print(f"aparelho: {self.nome}")
        print(f"preço: {self.preco:.2f}")
aparelho = Aparelhos("Smartphone",2500.00)
aparelho.mostrar()