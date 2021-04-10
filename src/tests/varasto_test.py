import unittest
from varasto import Varasto


class TestNegativeVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10, -5)

    def test_negatiivisella_varastolla_nolla_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivisella_saldolla_nolla_saldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestOverloadedVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, 20)

    def test_ylisuurella_saldolla_saldo_sama_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto.saldo, 10)

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ylisuuri_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_ei_muuta_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ylisuuri_ottaminen_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tulosta_varasto(self):
        self.varasto.lisaa_varastoon(8)
        #print(self.varasto)
        self.assertEqual("saldo = 8, vielä tilaa 2", str(self.varasto))
