#criando uma classe
class Pessoa:


#criando metodo construtor(é executado quando criamos o objeto)

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

#metodo para mostrar os dados
#atributos = caracteristicas ex: nome, idade
#metodos = ações ex: andar, correr

    def apresentar(self):
        print(f"ola, meu nome é {self.nome}")
        print(f"minha idade é {self.idade}")

#criando objeto(uma pessoa)

p1 = Pessoa("yuri",17)

#chamar metodo
p1.apresentar()
