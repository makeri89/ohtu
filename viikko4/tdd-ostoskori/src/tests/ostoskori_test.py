import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote('maito', 3)
        self.vichy = Tuote('vichy', 4)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        
        self.assertEqual(self.kori.hinta(), 3)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.vichy)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.vichy)
        
        tuotteiden_hinta = self.maito.hinta() + self.vichy.hinta()
        
        self.assertEqual(self.kori.hinta(), tuotteiden_hinta)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        
        hinta = self.maito.hinta() * 2
        
        self.assertEqual(self.kori.hinta(), hinta)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 1)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        
        ostos = self.kori.ostokset()[0]
        
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.vichy)
        
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 2)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 1)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_tuote_jolla_oikeat_tiedot(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        
        ostos = self.kori.ostokset()[0]
        
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)
