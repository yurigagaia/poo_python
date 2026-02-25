class turma():
    def __int__(self):
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"aluno: {self.alunos} \n media: {aluno.media()} {aluno.situacao()}")
