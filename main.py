from FilaFactory import FilaFactory
from Constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA

fila1 = FilaFactory.pega_fila(TIPO_FILA_NORMAL)
fila1.atualiza_fila()
fila1.atualiza_fila()
fila1.atualiza_fila()
print(fila1.chama_cliente(8))
print(fila1.chama_cliente(15))

fila2 = FilaFactory.pega_fila(TIPO_FILA_PRIORITARIA)
fila2.atualiza_fila()
fila2.atualiza_fila()
fila2.atualiza_fila()
print(fila2.chama_cliente(6))
print(fila2.chama_cliente(2))
