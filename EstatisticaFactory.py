from typing import Union

from Constantes import TIPO_ESTATISTICA_RESUMIDA, TIPO_ESTATISTICA_DETALHADA
from EstatisticaResumida import EstatisticaResumida
from EstatisticaDetalhada import EstatisticaDetalhada


class EstatisticaFactory:

    @staticmethod
    def gera_estatitica(
            tipo_estatisitca: str,
            dia: str,
            agencia: int
    ) -> Union[(
            EstatisticaResumida, EstatisticaDetalhada
    )]:
        if tipo_estatisitca == TIPO_ESTATISTICA_RESUMIDA:
            return EstatisticaResumida(dia, agencia)
        if tipo_estatisitca == TIPO_ESTATISTICA_DETALHADA:
            return EstatisticaDetalhada(dia, agencia)
        else:
            raise NotImplementedError('Estatística não existente')
