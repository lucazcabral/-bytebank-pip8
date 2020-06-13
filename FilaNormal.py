# -*-encoding: UTF-8 -*-
from FilaBase import FilaBase
from Constantes import PREFIXO_FILA_NORMAL


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.set_senha_atual(f'{PREFIXO_FILA_NORMAL}{self.get_codigo()}')
