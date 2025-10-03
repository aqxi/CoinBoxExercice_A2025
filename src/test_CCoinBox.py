import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_pass(self):
        pass

    def test_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_retourne_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        piece = coinBox.retourne_monnaie()
        self.assertEqual(coinBox.get_vente_permise(), False)
        self.assertEqual(piece, 1)

    def test_permet_une_double_vente(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.vente()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_vente_deduit_correctement_monnaie(self):
        """Test pour s'assurer qu'une vente SOUSTRAIT la monnaie et ne l'ADDITIONNE pas"""
        coinBox = CCoinBox()
        # Ajouter 4 pièces pour avoir assez pour une vente
        coinBox.ajouter_25c()  # 1 pièce
        coinBox.ajouter_25c()  # 2 pièces
        coinBox.ajouter_25c()  # 3 pièces
        coinBox.ajouter_25c()  # 4 pièces
        
        # Vérifier l'état avant vente
        monnaie_avant = coinBox.get_monnaie_courante()
        self.assertEqual(monnaie_avant, 4)
        
        # Effectuer une vente
        coinBox.vente()
        
        # Vérifier que la monnaie a DIMINUÉ (pas augmenté)
        monnaie_apres = coinBox.get_monnaie_courante()
        self.assertEqual(monnaie_apres, 2)  # 4 - 2 = 2
        
        # S'assurer que la monnaie après vente est inférieure à avant
        self.assertLess(monnaie_apres, monnaie_avant, 
                       "La monnaie courante doit diminuer après une vente, pas augmenter!")