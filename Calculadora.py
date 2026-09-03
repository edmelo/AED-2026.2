"""Operacoes aritmeticas basicas de uma calculadora."""

import numpy as np


class Calculadora:
	"""Calculadora com as quatro operacoes aritmeticas elementares."""

	def soma(self, primeiro, segundo):
		"""Retorna a soma de dois numeros."""
		return primeiro + segundo

	def subtracao(self, primeiro, segundo):
		"""Retorna a diferenca entre dois numeros."""
		return primeiro - segundo

	def multiplicacao(self, primeiro, segundo):
		"""Retorna o produto de dois numeros."""
		return primeiro * segundo

	def divisao(self, primeiro, segundo):
		"""Retorna o quociente usando a funcao de divisao do NumPy."""
		if segundo == 0:
			raise ZeroDivisionError("nao e possivel dividir por zero")
		return np.divide(primeiro, segundo)
