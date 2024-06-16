class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.disciplinas = []

    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade

    def atualizar_info(self, novo_nome, nova_idade):
        self.nome = novo_nome
        self.idade = nova_idade

    def consultar_disciplinas(self):
        return self.disciplinas