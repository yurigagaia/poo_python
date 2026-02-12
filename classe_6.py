class Plano:
    def __init__(self,nome,mensalidade):
        self.nome = nome
        self.mensalidade  = mensalidade
    def mostrar(self):
        print(f"plano: {self.nome}")
        print(f"mensalidade: {self.mensalidade} reais")
planos = Plano("pobre",20)
planos.mostrar()