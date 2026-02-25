class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def contar_tudo(self):
        return(f"o nome: {self.nome} \no total de produtos é {self.preco * self.quantidade}")

produto1 = Produto("bolsa",19, 200)
print(produto1.contar_tudo())