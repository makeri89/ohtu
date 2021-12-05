class Nollaus:
    def __init__(self, sovelluslogiikka, lue_arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_arvo = lue_arvo
        self._arvo = 0
        
    def suorita(self):
        self.arvo = self._lue_arvo()
        self._sovelluslogiikka.nollaa()
        
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._arvo)