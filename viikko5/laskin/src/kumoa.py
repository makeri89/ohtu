class Kumoa:
    def __init__(self, sovelluslogiikka, hae_edellinen_komento):
        self._sovelluslogiikka = sovelluslogiikka
        self._hae_edellinen_komento = hae_edellinen_komento
        
    def suorita(self):
        edellinen_komento = self._hae_edellinen_komento()
        edellinen_komento.kumoa()