"""
Implemente:
Desenvolva a estrutura de um sistema para cadastrar os seguintes dados
de professores e funcionários de uma instituição de ensino:
nome, quantidade de dependentes, salário fixo, quantidade de turmas e valor por turma.
"""
from abc import ABC


class Pessoa(ABC):
    ct = 0
    lista = []

    # retorna a quantidade de pessoas criadas
    @classmethod
    def qt_pessoa(cls):
        return cls.ct

    # retorna a lista de pessoas
    @classmethod
    def get_lista(cls):
        return cls.ct

    # inicia uma pessoa
    def __init__(self, nome, dependente):
        self.nome = nome
        if dependente < 0:
            raise ValueError("O numero de dependentes não pode ser negativo")
        self.dependente = dependente
        Pessoa.ct = Pessoa.ct + 1
        Pessoa.lista.append(self)

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_dependente(self):
        return self.dependente

    def set_dependente(self, novo_dependente):
        if novo_dependente < 0:
            raise ValueError("O numero de dependentes não pode ser negativo")
        self.dependente = novo_dependente

    # mostra os dados da pessoa
    def mostra_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Número de dependentes: {self.dependente}")

    def val_extra(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome="", dependente=0, qtd_turma=0, valor_turma=0):
        super().__init__(nome, dependente)
        self.qtd_turma = qtd_turma
        self.valor_turma = valor_turma

    def get_qtd_turma(self):
        return self.qtd_turma

    def set_qtd_turma(self, novo_qtd_turma):
        if novo_qtd_turma < 0:
            raise ValueError("O numero de dependentes não pode ser negativo")
        self.qtd_turma = novo_qtd_turma

    def get_valor_turma(self):
        return self.valor_turma

    def set_valor_turma(self, novo_valor_turma):
        self.valor_turma = novo_valor_turma

    # calcula o rendimento do professor
    def rendimentos(self):
        rendimento = self.qtd_turma * self.valor_turma
        return rendimento

    # calcula o salário do professor
    def salario(self):
        salario = self.val_extra() + self.rendimentos()
        return salario

    # calcula o valor extra baseano no numero de dependentes
    def val_extra(self):
        valor_x = self.dependente * 100
        return valor_x


class Funcionario(Pessoa):
    def __init__(self, nome="", dependente=0, salario_fixo=0):
        super().__init__(nome, dependente)
        self.salario_fixo = salario_fixo

    def get_salario_fixo(self):
        return self.salario_fixo

    def set_salario_fixo(self, novo_salario):
        self.salario_fixo = novo_salario

    # calcula o salário do funcionário
    def salario_f(self):
        salario_f = self.val_extra() + self.salario_fixo
        return salario_f

    # calcula o valor extra baseado no número de dependentes
    def val_extra(self):
        valor_x = self.dependente * 100
        return valor_x


if __name__ == '__main__':
    P1 = Pessoa("Fernando", 2)
    Pr1 = Professor("Raul", 2, 8, 900)
    Pr2 = Professor("Marcio", 9)
    Pr3 = Professor()
    Pr4 = Professor("Jair", qtd_turma=9)
    Pr4.set_nome("Bruno")
    Pr4.set_qtd_turma(5)
    print(Pr1)
    Pr1.get_qtd_turma()
    Pr1.set_qtd_turma(6)
    P1.mostra_dados()
    print(Pr1.rendimentos())

    F1 = Funcionario("Marcelo", 4, 1700)
    F2 = Funcionario("Luna", 4)
    F3 = Funcionario("Ronaldo")
    print(F1.get_nome())
    F1.set_salario_fixo(2300)
    F1.mostra_dados()

    print(Pr1.val_extra())
    print(Pr1.rendimentos())
    print(Pr1.salario())
