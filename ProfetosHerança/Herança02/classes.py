from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    # decorador de metodos
    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} já esta matridulado !")


    def estudar(self):
        print(f"O {self.nome} esta estudando {self.curso}")



class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} dando aula de {self.especialidade}")

    def estudar(self):
        print(f"O {self.nome} esta estudando {self.especialidade}")



class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionario {self.nome}, já chegou !")

    def estudar(self):
        print(f"O {self.nome} quer estudar mais sobre seu cargo !")