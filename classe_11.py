ano_atual = 2026
class pessoa:
    def __init__(self,nome,data,apelido):
        self.nome = nome
        self.data = data
        self.apelido = apelido
    def calcular_data(self):
        idade = ano_atual - self.data
    def mostrar_nome(self):
        print(f"nome: {self.nome}")
        print(f"apelido: {self.apelido}")
    def mostrar_idade():
        print("")