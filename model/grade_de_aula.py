class GradeDeAula:
    def __init__(self, aluno, disciplina, professor, sala_de_aula):
        self.aluno = aluno
        self.disciplina = disciplina
        self.professor = professor
        self.sala_de_aula = sala_de_aula
        self.notas = {}

    def adicionar_nota(self, dic, nota):
        self.notas[dic] = nota

    def editar_nota(self, dic, nova_nota):
        if dic in self.notas:
            self.notas[dic] = nova_nota
        else:
            print("Nota não encontrada.")

    def remover_nota(self, dic):
        if dic in self.notas:
            del self.notas[dic]
        else:
            print("Nota não encontrada.")

    def consultar_notas(self):
        return self.notas

    def __str__(self):
        notas_str = ", ".join(f"{dic}: {nota}" for dic, nota in self.notas.items())
        return (f"Aluno: {self.aluno.nome}, Disciplina: {self.disciplina.nome}, "
                f"Professor: {self.professor.nome}, Sala: {self.sala_de_aula.numero}, Notas: {notas_str}")
