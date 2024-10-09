import unittest
import test_12_3

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

Ruunner = unittest.TextTestRunner(verbosity=2)
Ruunner.run(calcST)

