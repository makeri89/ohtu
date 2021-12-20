from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()
    
    
    def _toisen_siirto(self, ekan_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f'Tietokone valitsi {siirto}')
        return siirto