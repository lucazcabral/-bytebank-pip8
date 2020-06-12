# -*-encoding: UTF-8 -*-
class FilaPrioritaria:
    __codigo: int = 0
    __fila: list = []
    __clientes_atendidos: list = []
    __senha_atual: str = ''

    def gera_senha_atual(self) -> None:
        self.__senha_atual = f'PR{self.__codigo}'

    def reseta_fila(self) -> None:
        if self.__codigo >= 100:
            self.__codigo = 0;
        else:
            self.__codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.__fila.append(self.__senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: int = self.__fila.pop(0)
        self.__clientes_atendidos.append(cliente_atual)
        return f'Caixa {caixa} livre. Senha {cliente_atual} chamada.'

    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        stats: dict = {}
        if flag != 'detail':
            stats = {f'{agencia} - {dia}': len(self.__clientes_atendidos)}
        else:
            stats['dia'] = dia
            stats['agencia'] = agencia
            stats['clientes atendidos'] = self.__clientes_atendidos
            stats['quantidade de clientes atendidos'] = len(self.__clientes_atendidos)

        return stats
