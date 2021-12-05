class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._arvo = 0
        
    def suorita(self):
        self._arvo = int(self._lue_syote())
        self._sovelluslogiikka.plus(self._arvo)
        
    def kumoa(self):
        self._sovelluslogiikka.miinus(self._arvo)