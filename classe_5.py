class roupa:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        print(f"peça: {self.nome}")
        print(f"preço: {self.preco:.2f}")

peca = roupa("jens",59.90)
peca.mostrar()