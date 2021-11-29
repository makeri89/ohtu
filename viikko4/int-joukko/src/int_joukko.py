OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is not None and self.tarkista_syote(kapasiteetti):
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        self.kapasiteetti = kapasiteetti or OLETUSKAPASITEETTI
        
        if kasvatuskoko is not None and self.tarkista_syote(kasvatuskoko):
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0
        
    def tarkista_syote(self, syote):
        return not isinstance(syote, int) or syote < 0
            
    def kuuluuko_joukkoon(self, n):
        return n in self.lukujono
    
    def kasvata_lukujonoa(self):
        self.lukujono.extend([0] * self.kasvatuskoko)

    def lisaa_alkio(self, n):
        if self.kuuluuko_joukkoon(n): 
            return
        
        if self.alkioiden_lkm == len(self.lukujono):
            self.kasvata_lukujonoa()
            
        self.lukujono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        

    def poista_alkio(self, n):
        indeksi = -1 if not self.kuuluuko_joukkoon(n) else self.lukujono.index(n)
                
        if indeksi == -1: return
        
        self.lukujono.pop(indeksi)
        self.lukujono.append(0)
        self.alkioiden_lkm -= 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def muuta_lukujonoksi(self):
        return [i for i in self.lukujono if i != 0]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.muuta_lukujonoksi()
        b_taulu = b.muuta_lukujonoksi()

        for luku in a_taulu:
            x.lisaa_alkio(luku)

        for luku in b_taulu:
            x.lisaa_alkio(luku)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.muuta_lukujonoksi()
        b_taulu = b.muuta_lukujonoksi()
        
        for luku in a_taulu:
            if luku in b_taulu:
                y.lisaa_alkio(luku)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.muuta_lukujonoksi()
        b_taulu = b.muuta_lukujonoksi()
        
        for luku in a_taulu:
            if luku not in b_taulu:
                z.lisaa_alkio(luku)

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuotos = "{"
        for i in range(self.alkioiden_lkm - 1):
            tuotos += str(self.lukujono[i]) + ", "
        tuotos += str(self.lukujono[self.alkioiden_lkm - 1])
        tuotos += "}"
        return tuotos
