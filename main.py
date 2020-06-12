from FilaNormal import FilaNormal
from FilaPrioritaria import FilaPrioritaria

fila_normal = FilaNormal()
fila_normal.atualiza_fila()
fila_normal.atualiza_fila()
fila_normal.atualiza_fila()
print(fila_normal.chama_cliente(5))
print(fila_normal.chama_cliente(10))


fila_prioritaria = FilaPrioritaria()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
print(fila_prioritaria.chama_cliente(3))
print(fila_prioritaria.chama_cliente(7))
