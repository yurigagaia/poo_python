class produto():
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco_original = preco
        self.preco = preco
    
    def aplicar_desconto(self,percentual):
    
        desconto = (self.preco * percentual) /100
        self.preco -= desconto

    def mostrar(self,):
        print(f"nome do produto: {self.nome}")
        print(f"valor: {self.preco_original}")
        print(f"valor com desconto {self.preco}")

produto1 = produto("aspirador de pó", 1500)
produto1.aplicar_desconto(20)
produto1.mostrar()