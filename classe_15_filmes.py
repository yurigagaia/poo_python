longo = 120
class Filme:
    def __init__(self,titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar(self):
        print(f"titulo: {self.titulo} duracao: {self.duracao}")

    def longo(self):
        if self.duracao >= longo:
            print("True")
        else:
            print("False")

filme1 = Filme("evagelion",120)
filme1.mostrar()
filme1.longo()


class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar(self):
        return f"Título: {self.titulo} | Duração: {self.duracao} min"

    def eh_longo(self, tempo_minimo=120):
        return self.duracao >= tempo_minimo


# Criando objeto
filme1 = Filme("Evangelion", 120)

# Mostrando informações
print(filme1.mostrar())

# Verificando se é longo
print(filme1.eh_longo())