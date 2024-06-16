import pandas as pd
from controller.sistema_gerenciador import SistemaGerenciador
grade_de_auladf = pd.read_csv('data/grade_de_aula.csv', na_values=None, keep_default_na=False)
alunosdf = pd.read_csv('data/alunos.csv')
professordf = pd.read_csv('data/professores.csv')
materiasdf = pd.read_csv('data/materias.csv')
sala_de_auladf = pd.read_csv('data/sala_de_aula.csv')

'''
Iniciar no terminal usando: python -m view.main






'''

sistema = SistemaGerenciador()
pula_espera=0
while True:
    if pula_espera != 0:espera = input("Aperte enter para continuar")
    pula_espera+=1
    print("\nOpções:")
    print("1. Aluno")
    print("2. Professor")
    print("3. Disciplina")
    print("4. Sala de Aula")
    print("5. Grade de Aula")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("1. Registrar aluno")
        print("2. Consultar alunos")
        print("3. Editar alunos")
        print("4. Excluir alunos")
        opcao2 = input("Escolha uma opção: ")
        if opcao2 == "1":
                aluno = sistema.registrar_aluno()
        elif opcao2 == "2":
            for index, row in alunosdf.iterrows():
                print(', '.join(map(str, row.values)))
        elif opcao2 == "3":
            sistema.editar_aluno()
        elif opcao2 == "4":
            sistema.excluir_aluno()
        else:
            print("Opção inválida. Tente novamente.")
    elif opcao == "2":
        print("1. Registrar professor")
        print("2. Consultar professor")
        print("3. Editar professor")
        print("4. Excluir professor")
        opcao2 = input("Escolha uma opção: ")
        if opcao2 == "1":
                professor = sistema.registrar_professor()
        elif opcao2 == "2":
            for index, row in professordf.iterrows():
                print(', '.join(map(str, row.values)))
        elif opcao2 == "3":
            sistema.edita_professor()
        elif opcao2 == "4":
            sistema.excluir_professor()
        else:
            print("Opção inválida. Tente novamente.")
    elif opcao == "3":
        print("1. Registrar disciplina")
        print("2. Consultar disciplina")
        print("3. Editar disciplina")
        print("4. Excluir disciplina")
        opcao2 = input("Escolha uma opção: ")
        if opcao2 == "1":
                disciplina = sistema.registrar_disciplina()
        elif opcao2 == "2":
            for index, row in materiasdf.iterrows():
                print(', '.join(map(str, row.values)))
        elif opcao2 == "3":
            sistema.editar_disciplina()
        elif opcao2 == "4":
            sistema.excluir_disciplina()
    elif opcao == "4":
        print("1. Registrar sala de aula")
        print("2. Consultar sala de aula")
        print("3. Editar sala de aula")
        print("4. Excluir sala de aula")
        opcao2 = input("Escolha uma opção: ")
        if opcao2 == "1":
                sala_de_aula = sistema.registrar_sala_de_aula()
        elif opcao2 == "2":
            for index, row in sala_de_auladf.iterrows():
                print(', '.join(map(str, row.values)))
        elif opcao2 == "3":
            sistema.editar_sala_de_aula()
        elif opcao2 == "4":
            sistema.excluir_sala_de_aula()
    elif opcao == "5":
        print("1. Registrar Grade de Aula")
        print("2. Consultar Grade de Aula")
        print("3. Editar Grade de Aula")
        print("4. Excluir Grade de Aula")
        opcao2 = input("Escolha uma opção: ")
        if opcao2 == "1":
                sistema.registrar_grade_de_aula()
        elif opcao2 == "2":
            for index, row in grade_de_auladf.iterrows():
                print(', '.join(map(str, row.values)))
        elif opcao2 == "3":
            sistema.editar_grade_aula()
        elif opcao2 == "4":
            sistema.excluir_grade_de_aula()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")