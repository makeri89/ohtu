from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def __init__(self, muistin_koko):
        self._tekoaly = TekoalyParannettu(muistin_koko)
        
    def _toisen_siirto(self, ekan_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f'Tietokone valitsi: {siirto}')
        self._tekoaly.aseta_siirto(ekan_siirto)
        return siirto