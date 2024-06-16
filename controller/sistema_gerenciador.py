import pandas as pd
from model.aluno import Aluno
from model.professor import Professor
from model.disciplina import Disciplina
from model.sala_de_aula import SalaDeAula
from model.grade_de_aula import GradeDeAula

class SistemaGerenciador:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self.salas_de_aula = []
        self.grades_de_aula = []

    def registrar_aluno(self):
        alunosdf = pd.read_csv('data/alunos.csv')
        alunosdf = alunosdf.set_index('nome')

        nome = input("Nome do aluno: ")
        idade = int(input("Idade do aluno: "))
        matricula = input("Matrícula do aluno: ")
        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        print("Aluno registrado com sucesso!")

        alunosdf.loc[nome] = [idade, matricula]
        alunosdf.to_csv('data/alunos.csv')

        return aluno

    def registrar_professor(self):
        professoresdf = pd.read_csv('data/professores.csv')
        professoresdf = professoresdf.set_index('nome')

        nome = input("Nome do professor: ")
        idade = int(input("Idade do professor: "))
        professor = Professor(nome, idade)
        self.professores.append(professor)
        print(f"Professor {professor.nome} registrado com sucesso!")

        professoresdf.loc[nome] = [idade]
        professoresdf.to_csv('data/professores.csv')

        return professor

    def registrar_disciplina(self):
        materiasdf = pd.read_csv('data/materias.csv')
        materiasdf = materiasdf.set_index('nome')

        nome = input("Nome da disciplina: ")
        codigo = input("Código da disciplina: ")
        disciplina = Disciplina(nome, codigo)
        self.disciplinas.append(disciplina)
        print("Disciplina registrada com sucesso!")

        materiasdf.loc[nome] = [codigo]
        materiasdf.to_csv('data/materias.csv')

        return disciplina

    def registrar_sala_de_aula(self):
        sala_de_auladf = pd.read_csv('data/sala_de_aula.csv')
        sala_de_auladf = sala_de_auladf.set_index('numero')

        numero = input("Número da sala de aula: ")
        capacidade = int(input("Capacidade da sala de aula: "))
        sala_de_aula = SalaDeAula(numero, capacidade)
        self.salas_de_aula.append(sala_de_aula)
        print("Sala de aula registrada com sucesso!")

        sala_de_auladf.loc[numero] = [capacidade]
        sala_de_auladf.to_csv('data/sala_de_aula.csv')

        return sala_de_aula
    
    def registrar_grade_de_aula(self):
        grade_de_auladf = pd.read_csv('data/grade_de_aula.csv')
        alunosdf = pd.read_csv('data/alunos.csv')
        nomeAluno = alunosdf['nome']
        professordf = pd.read_csv('data/professores.csv')
        nomeProfessor = professordf['nome']
        materiasdf = pd.read_csv('data/materias.csv')
        nomeMateria = materiasdf['nome']
        sala_de_auladf = pd.read_csv('data/sala_de_aula.csv')
        numSalaDeAula = sala_de_auladf['numero']
        grade_de_auladf = grade_de_auladf.set_index('aluno')


        print("Alunos disponíveis:")
        for nome in nomeAluno:
            print(nome)
        aluno = input("Selecione o aluno (Nome completo): ")

        print("Disciplinas disponíveis:")
        for nome in nomeMateria:
            print(nome)
        disciplina = input("Selecione a disciplina (Nome da disciplina): ")

        print("Professores disponíveis:")
        for nome in nomeProfessor:
            print(nome)
        professor = input("Selecione o professor (Nome completo): ")

        print("Salas de aula disponíveis:")
        for numero in numSalaDeAula:
            print(numero)
        sala_de_aula = input("Selecione a sala de aula (Número): ")

        nota = float(input("Insira nota do aluno:"))
        print("Grade de aula registrada com sucesso!")


        grade_de_auladf.loc[aluno] = [disciplina, professor, sala_de_aula, nota]
        grade_de_auladf.to_csv('data/grade_de_aula.csv')
    
    def editar_aluno(self):
        alunosdf = pd.read_csv('data/alunos.csv')
        nomeAluno = alunosdf['nome']

        print("\nAlunos:")
        for nome in nomeAluno:
            print(nome)
        nome_buscado = input("Digite o nome do aluno que deseja editar: ")
        if nome_buscado in alunosdf['nome'].values:
            novo_nome = input("Novo nome do aluno: ")
            nova_idade = int(input("Nova idade do aluno: "))
            nova_matricula = int(input("Nova matrícula do aluno: "))
            alunosdf.loc[alunosdf['nome'] == nome_buscado, ['nome', 'idade', 'matricula']] = [novo_nome, nova_idade, nova_matricula]
            alunosdf.to_csv('data/alunos.csv', index=False)
        else:
            print("Aluno não encontrado.")
        

    def edita_professor(self):
        professoresdf = pd.read_csv('data/professores.csv')
        nomeProfessor = professoresdf['nome']

        print("\nProfessores:")
        for nome in nomeProfessor:
            print(nome)
        nome_buscado = input("Digite o nome do professor que deseja editar: ")
        if nome_buscado in professoresdf['nome'].values:
            novo_nome = input("Novo nome do professor: ")
            nova_idade = int(input("Nova idade do professor: "))
            professoresdf.loc[professoresdf['nome'] == nome_buscado, ['nome', 'idade']] = [novo_nome, nova_idade]
            professoresdf.to_csv('data/professores.csv', index=False)
        else:
            print("Professor não encontrado.")

    def editar_disciplina(self):
        materiasdf = pd.read_csv('data/materias.csv')
        nomeMateria = materiasdf['nome']

        print("\nDisciplinas:")
        for nome in nomeMateria:
            print(nome)
        nome_buscado = input("Nome da disciplina a ser editada: ")
        if nome_buscado in materiasdf['nome'].values:
            novo_nome = input("Novo nome da matéria: ")
            novo_codigo = int(input("Novo código da matéria: "))
            materiasdf.loc[materiasdf['nome'] == nome_buscado, ['nome', 'codigo']] = [novo_nome, novo_codigo]
            materiasdf.to_csv('data/materias.csv', index=False)
        else:
            print("Matéria não encontrada.")

    def editar_sala_de_aula(self):
        sala_de_auladf = pd.read_csv('data/sala_de_aula.csv')
        numSala = sala_de_auladf['numero']

        print("\nSalas de Aula:")
        for numero in numSala:
            print(numero)
        numero_buscado = input("Número da sala de aula a ser editada: ")
        if numero_buscado in sala_de_auladf['numero'].values:
            novo_num = int(input("Novo número da sala: "))
            nova_capacidade = int(input("Nova capacidade da sala: "))
            sala_de_auladf.loc[sala_de_auladf['numero'] == numero_buscado, ['numero', 'capacidade']] = [novo_num, nova_capacidade]
            sala_de_auladf.to_csv('data/sala_de_aula.csv', index=False)
        else:
            print("Sala não encontrada.")
    
    def editar_grade_aula(self):
        alunosdf = pd.read_csv('data/alunos.csv')
        disciplinasdf = pd.read_csv('data/materias.csv')
        professoresdf = pd.read_csv('data/professores.csv')
        salasdf = pd.read_csv('data/sala_de_aula.csv')
        grade_de_auladf = pd.read_csv('data/grade_de_aula.csv', na_values=None, keep_default_na=False)
        grade_de_auladf.index = range(1, len(grade_de_auladf) + 1)

        print("Grades de aula registradas:")
        print(grade_de_auladf.to_string(index=True))

        grade_index = int(input("Selecione a grade de aula para editar: "))

        if grade_index not in grade_de_auladf.index:
            print("Índice inválido.")
            return

        print("O que deseja editar?")
        print("1. Aluno")
        print("2. Disciplina")
        print("3. Professor")
        print("4. Sala de Aula")
        print("5. Nota")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Alunos disponíveis:")
            for index, row in alunosdf.iterrows():
                print(', '.join(map(str, row.values)))
            novo_aluno = input("Novo nome do aluno: ")
            grade_de_auladf.loc[grade_index, 'aluno'] = novo_aluno
            grade_de_auladf.to_csv('data/grade_de_aula.csv', index=False)
        elif opcao == 2:
            print("Disciplinas disponíveis:")
            for index, row in disciplinasdf.iterrows():
                print(', '.join(map(str, row.values)))
            nova_disciplina = input("Novo nome da disciplina: ")
            grade_de_auladf.loc[grade_index, 'disciplina'] = nova_disciplina
            grade_de_auladf.to_csv('data/grade_de_aula.csv', index=False)
        elif opcao == 3:
            print("Professores disponíveis:")
            for index, row in professoresdf.iterrows():
                print(', '.join(map(str, row.values)))
            novo_professor = input("Novo nome do professor: ")
            grade_de_auladf.loc[grade_index, 'professor'] = novo_professor
            grade_de_auladf.to_csv('data/grade_de_aula.csv', index=False)
        elif opcao == 4:
            print("Salas de aula disponíveis:")
            for index, row in salasdf.iterrows():
                print(', '.join(map(str, row.values)))
            nova_sala = input("Novo número da sala de aula: ")
            grade_de_auladf.loc[grade_index, 'sala de aula'] = nova_sala
            grade_de_auladf.to_csv('data/grade_de_aula.csv', index=False)
        elif opcao == 5:
            nota_atual = grade_de_auladf.loc[grade_index, 'nota']
            print(f"Nota atual: {nota_atual}")
            print("O que deseja fazer?")
            print("1. Adicionar/Editar Nota")
            print("2. Remover Nota")
            nota_opcao = int(input("Escolha uma opção: "))

            if nota_opcao == 1:
                nova_nota = float(input("Nova nota: "))
                grade_de_auladf.loc[grade_index, 'nota'] = nova_nota
                print("Nota adicionada/editada com sucesso!")
            elif nota_opcao == 2:
                grade_de_auladf.loc[grade_index, 'nota'] = ""
                print("Nota removida com sucesso!")
            else:
                print("Opção inválida.")
                return

        else:
            print("Opção inválida. Tente novamente.")
            return
        
        grade_de_auladf.to_csv('data/grade_de_aula.csv', index=False)
        print("Grade de aula atualizada com sucesso!")

    def excluir_aluno(self):
        alunosdf = pd.read_csv('data/alunos.csv')

        print("Alunos: ")
        for index, row in alunosdf.iterrows():
                print(', '.join(map(str, row.values)))

        aluno_nome = input("Nome do aluno para excluir: ")
        if aluno_nome in alunosdf['nome'].values:
            indices = alunosdf[alunosdf['nome'] == aluno_nome].index
            alunosdf = alunosdf.drop(indices)
            alunosdf.to_csv('data/alunos.csv', index=False)
            print("Aluno excluído com sucesso.")
        else:
            print("Aluno não encontrado.")

    def excluir_professor(self):
        professoresdf = pd.read_csv('data/professores.csv')

        print("Professores: ")
        for index, row in professoresdf.iterrows():
                print(', '.join(map(str, row.values)))

        professor_nome = input("Nome do professor para excluir: ")
        if professor_nome in professoresdf['nome'].values:
            indices = professoresdf[professoresdf['nome'] == professor_nome].index
            professoresdf = professoresdf.drop(indices)
            professoresdf.to_csv('data/professores.csv', index=False)
            print("Professor excluído com sucesso.")
        else:
            print("Professor não encontrado.")

    def excluir_disciplina(self):
        materiasdf = pd.read_csv('data/materias.csv')

        print("Disciplinas: ")
        for index, row in materiasdf.iterrows():
                print(', '.join(map(str, row.values)))

        materia_nome = input("Nome da disciplina para excluir: ")
        if materia_nome in materiasdf['nome'].values:
            indices = materiasdf[materiasdf['nome'] == materia_nome].index
            materiasdf = materiasdf.drop(indices)
            materiasdf.to_csv('data/materias.csv', index=False)
            print("Disciplina excluída com sucesso.")
        else:
            print("Disciplina não encontrada.")

    def excluir_sala_de_aula(self):
        sala_de_auladf = pd.read_csv('data/sala_de_aula.csv')

        print("Salas de Aula: ")
        for index, row in sala_de_auladf.iterrows():
                print(', '.join(map(str, row.values)))

        sala_num = int(input("Número da sala para excluir: "))
        if sala_num in sala_de_auladf['numero'].values:
            indices = sala_de_auladf[sala_de_auladf['numero'] == sala_num].index
            sala_de_auladf = sala_de_auladf.drop(indices)
            sala_de_auladf.to_csv('data/sala_de_aula.csv', index=False)
            print("Sala de aula excluída com sucesso.")
        else:
            print("Sala de aula não encontrada.")

    def excluir_grade_de_aula(self):
        alunosdf = pd.read_csv('data/alunos.csv')
        grade_de_auladf = pd.read_csv('data/grade_de_aula.csv')

        print("\nAlunos:")
        for index, row in alunosdf.iterrows():
                print(', '.join(map(str, row.values)))

        aluno_nome = input("Nome do aluno para excluir grade de aula: ")
        if aluno_nome in grade_de_auladf['aluno'].values:
            indices = grade_de_auladf[grade_de_auladf['aluno'] == aluno_nome].index
            grade_de_auladf = grade_de_auladf.drop(indices)
            grade_de_auladf.to_csv('data/grade_de_aula.csv', index=False)
            print("Grade de aula excluída com sucesso.")
        else:
            print("Aluno não encontrado na grade de aula.")