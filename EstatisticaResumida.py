from typing import Dict, Union, List

from EstatisticaBase import EstatisticaBase


class EstatisticaResumida(EstatisticaBase):

    def roda_estatistica(
            self,
            clientes_atendidos: List[str]
    ) -> Dict[str, Union[List[str], str, int]]:

        estatistica: Dict[str, Union[List[str], str, int]] = {}
        chave_agencia_dia: str = f'{self.get_agencia()} - {self.get_dia()}'
        estatistica[chave_agencia_dia] = len(clientes_atendidos)

        return estatistica
