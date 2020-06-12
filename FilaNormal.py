# -*-encoding: UTF-8 -*-
from FilaBase import FilaBase


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.set_senha_atual(f'NM{self.get_codigo()}')

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.get_fila().append(self.get_senha_atual())

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.get_fila().pop(0)
        self.get_clientes_atendidos().append(cliente_atual)
        return f'Caixa {caixa} livre. Senha {cliente_atual} chamada.'

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
