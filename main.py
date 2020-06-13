from Constantes import TIPO_FILA_NORMAL, \
    TIPO_FILA_PRIORITARIA, \
    TIPO_ESTATISTICA_RESUMIDA, \
    TIPO_ESTATISTICA_DETALHADA
from FilaFactory import FilaFactory
from EstatisticaFactory import EstatisticaFactory


# Gera dados para FILA 1
fila1 = FilaFactory.pega_fila(TIPO_FILA_NORMAL)
fila1.atualiza_fila()
fila1.atualiza_fila()
fila1.atualiza_fila()
print(fila1.chama_cliente(10))
print(fila1.chama_cliente(15))

estatisticaResumida = EstatisticaFactory.gera_estatitica(
    TIPO_ESTATISTICA_RESUMIDA,
    '15/01/2020',
    7787
)
print(fila1.estatistica(estatisticaResumida))


# Gera dados para FILA 2
fila2 = FilaFactory.pega_fila(TIPO_FILA_PRIORITARIA)
fila2.atualiza_fila()
fila2.atualiza_fila()
fila2.atualiza_fila()
fila2.atualiza_fila()
fila2.atualiza_fila()
fila2.atualiza_fila()
print(fila2.chama_cliente(6))
print(fila2.chama_cliente(2))
print(fila2.chama_cliente(1))
print(fila2.chama_cliente(3))

estatisticaDetalhada = EstatisticaFactory.gera_estatitica(
    TIPO_ESTATISTICA_DETALHADA,
    '01/01/2020',
    3123
)
print(fila2.estatistica(estatisticaDetalhada))
