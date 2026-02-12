import os
def limpar():
    os.system('cls')
limpar()
class item:
    def __init__(self,titulo,preco):
        self.titulo = titulo
        self.preco = preco

    def mostrar(self):
        print(f"titulo: {self.titulo}")  
        print(f"preço: {self.preco:.2f}") 
        
livro = item("evagelion",14.99)
livro.mostrar()
