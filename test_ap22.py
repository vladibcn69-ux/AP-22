"""Pruebas unitarias de [AP 22] Comprobador de congruencia."""

import unittest

from ap22_comprobador_congruencia import son_congruentes


class TestSonCongruentes(unittest.TestCase):
    def test_ejemplo_de_la_leccion(self):
        # 63 mod 10 = 3 y 83 mod 10 = 3; 63 - 83 = -20 = 10 * (-2)
        self.assertTrue(son_congruentes(63, 83, 10))

    def test_numeros_negativos(self):
        self.assertTrue(son_congruentes(-7, 3, 10))
        self.assertTrue(son_congruentes(-12, -2, 5))
        self.assertFalse(son_congruentes(-7, 4, 10))

    def test_a_igual_b(self):
        self.assertTrue(son_congruentes(42, 42, 7))

    def test_no_congruentes(self):
        self.assertFalse(son_congruentes(63, 84, 10))

    def test_modulo_uno(self):
        self.assertTrue(son_congruentes(5, 123, 1))

    def test_modulo_no_positivo(self):
        with self.assertRaises(ValueError):
            son_congruentes(63, 83, 0)
        with self.assertRaises(ValueError):
            son_congruentes(63, 83, -10)


if __name__ == "__main__":
    unittest.main()
