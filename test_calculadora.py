"""Testes unitarios para a classe Calculadora."""

import unittest

from Calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
	"""Testa as quatro operacoes aritmeticas da calculadora."""

	def setUp(self):
		self.calculadora = Calculadora()

	def test_soma(self):
		self.assertEqual(self.calculadora.soma(2, 3), 5)

	def test_subtracao(self):
		self.assertEqual(self.calculadora.subtracao(7, 4), 3)

	def test_multiplicacao(self):
		self.assertEqual(self.calculadora.multiplicacao(6, 5), 30)

	def test_divisao_com_numpy(self):
		self.assertAlmostEqual(self.calculadora.divisao(7, 2), 3.5)

	def test_divisao_por_zero(self):
		with self.assertRaises(ZeroDivisionError):
			self.calculadora.divisao(10, 0)


if __name__ == "__main__":
	unittest.main()