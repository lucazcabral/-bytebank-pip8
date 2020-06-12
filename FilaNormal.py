# -*-encoding: UTF-8 -*-
class FilaNormal:
    __codigo: int = 0
    __fila:list = []
    __clientes_atendidos: list = []
    __senha_atual: str = ''

    def gera_senha_atual(self) -> None:
        self.__senha_atual = f'NM{self.__codigo}'

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
        cliente_atual = self.__fila.pop(0)
        self.__clientes_atendidos.append(cliente_atual)
        return f'Caixa {caixa} livre. Senha {cliente_atual} chamada.'

    def estatistica(self, dia: str, agencia:str, flag:str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}':len(self.__clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.__clientes_atendidos
            estatistica['quantidade de clientes atendidos'] = len(self.__clientes_atendidos)

        return estatistica