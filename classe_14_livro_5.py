class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.paginas = 0

    def detalhes(self):
        print(f"titulo: {self.titulo}\n autor:{self.autor}")
    def longo(self,paginas):
        if paginas >= 300:
            print("true")
        else:
            print("false")
livro1 = Livro("evagelion","anno")
livro1.detalhes()
livro1.longo(299)