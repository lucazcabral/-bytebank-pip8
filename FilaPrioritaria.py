# -*-encoding: UTF-8 -*-
from FilaBase import FilaBase
from Constantes import PREFIXO_FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.set_senha_atual(f'{PREFIXO_FILA_PRIORITARIA}{self.get_codigo()}')

    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        estatistica: dict = {}
        if flag != 'detail':
            estatistica[f'{agencia} - {dia}'] = (
                len(self.get_clientes_atendidos())
            )
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.get_clientes_atendidos()
            estatistica['quantidade de clientes atendidos'] = (
                len(self.get_clientes_atendidos())
            )

        return estatistica
