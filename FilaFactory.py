from typing import Union

from Constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from FilaNormal import FilaNormal
from FilaPrioritaria import FilaPrioritaria


class FilaFactory:

    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        if tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo não cadastrado')
