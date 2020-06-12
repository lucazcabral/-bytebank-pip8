# -*-encoding: UTF-8 -*-
LIMITE_FILA = 100


class FilaBase:
    __codigo: int = 0
    __fila: list = []
    __clientes_atendidos: list = []
    __senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.__codigo >= LIMITE_FILA:
            self.__codigo = 0
        else:
            self.__codigo += 1

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
