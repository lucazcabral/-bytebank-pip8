import abc
from typing import Dict, Union, List


class EstatisticaBase:
    __dia: str
    __agencia: int

    # construtor
    def __init__(self, dia: str, agencia: int) -> None:
        self.__dia = dia
        self.__agencia = agencia

    # Getters and setters
    def set_dia(self, dia: str) -> None:
        self.__dia = dia

    def get_dia(self) -> str:
        return self.__dia

    def set_agencia(self, agencia: int) -> None:
        self.__agencia = agencia

    def get_agencia(self) -> int:
        return self.__agencia

    # Métodos Abstratos
    @abc.abstractmethod
    def roda_estatistica(
            self,
            clientes_atendidos: List[str]
    ) -> Dict[str, Union[List[str], str, int]]:
        ...
