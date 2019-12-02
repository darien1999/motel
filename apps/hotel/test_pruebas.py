import unittest
from pruebas import probar


class TestProbar(unittest.Testcase):
    def test_sumar(self):
        self.assertAlmostEqual(probar(3,5)8)
