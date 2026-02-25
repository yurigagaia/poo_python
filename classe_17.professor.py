class Professor:
    def __init__(self, nome, diciplina):
        self.nome = nome
        self.diciplina = diciplina
    
    def lecionar(self):
        print(f"professor: {self.nome} \nmateria: {self.diciplina}")
    
professor1 = Professor("frainy","filosofia")
professor1.lecionar()