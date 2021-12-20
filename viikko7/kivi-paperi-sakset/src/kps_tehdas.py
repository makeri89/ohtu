from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSTehdas():
    @staticmethod
    def luo_kps_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def luo_kps_tekoaly():
        return KPSTekoaly()
    
    @staticmethod
    def luo_kps_parempi_tekoaly(muisti):
        return KPSParempiTekoaly(muisti)