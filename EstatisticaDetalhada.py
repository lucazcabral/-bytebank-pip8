from typing import Dict, Union, List

from EstatisticaBase import EstatisticaBase


class EstatisticaDetalhada(EstatisticaBase):

    def roda_estatistica(
            self,
            clientes_atendidos: List[str]
    ) -> Dict[str, Union[List[str], str, int]]:

        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica['dia'] = self.get_dia()
        estatistica['agencia'] = self.get_agencia()
        estatistica['clientes atendidos'] = clientes_atendidos
        estatistica['quantidade de clientes atendidos'] = (
            len(clientes_atendidos)
        )

        return estatistica
