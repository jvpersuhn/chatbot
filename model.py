class Consulta:
    def __init__(self):
        self.especialidade = ''
        self.horario = ''
        self.nome = ''
        self.cpf = ''

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade

    def set_horario(self, horario):
        self.horario = horario

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_especialidade(self):
        return self.especialidade

    def get_horario(self):
        return self.horario

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf