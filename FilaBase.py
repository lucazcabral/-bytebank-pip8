# -*-encoding: UTF-8 -*-
import abc
from typing import Dict, Union, List

from Constantes import TAMANHO_MAXIMO_FILA, TAMANHO_MINIMO_FILA


class FilaBase(metaclass=abc.ABCMeta):
    __codigo: int = 0
    __fila: List[str] = []
    __clientes_atendidos: List[str] = []
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
    def estatistica(
            self,
            dia: str,
            agencia: str,
            flag: str) -> (Dict[str, Union[List[str], str, int]]):
        ...

    # Definição de metodos comuns
    def reseta_fila(self) -> None:
        if self.__codigo >= TAMANHO_MAXIMO_FILA:
            self.__codigo = TAMANHO_MINIMO_FILA
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
