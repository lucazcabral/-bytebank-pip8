# -*-encoding: UTF-8 -*-
import abc

LIMITE_FILA = 100


class FilaBase(metaclass=abc.ABCMeta):
    __codigo: int = 0
    __fila: list = []
    __clientes_atendidos: list = []
    __senha_atual: str = ''

    # Getters and Setters
    def get_codigo(self) -> int:
        return self.__codigo

    def get_fila(self) -> list:
        return self.__fila

    def get_clientes_atendidos(self) -> list:
        return self.__clientes_atendidos

    def get_senha_atual(self) -> str:
        return self.__senha_atual

    def set_senha_atual(self, senha_atual: str):
        self.__senha_atual = senha_atual

    # Definição de metodos abstratos
    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    @abc.abstractmethod
    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        ...

    # Definição de metodos comuns
    def reseta_fila(self) -> None:
        if self.__codigo >= LIMITE_FILA:
            self.__codigo = 0
        else:
            self.__codigo += 1

    def insere_cliente(self) -> None:
        self.get_fila().append(self.get_senha_atual())

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.get_fila().pop(0)
        self.get_clientes_atendidos().append(cliente_atual)
        return f'Caixa {caixa} livre. Senha {cliente_atual} chamada.'
