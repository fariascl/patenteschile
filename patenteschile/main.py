# patentevalida.py
# Autor: Alejandro (farias@8loop.cl)
# Esta librería genera patentes vehículares válidas
"""
for patentevalida import Patente
patentes = Patente()
print(patentes.generate(10))
"""

import sys
import rstr
import re

class Patente:
	def calculate_patente(self):
		words = rstr.xeger(r"[B-Z]{4}\d")
		number = rstr.xeger(r"[10-99]{1}")
		inthere = False
		filters = ['A','E','I','M','N','Ñ','O','Q','U']
		for word in words:
			for filter in filters:
				if (word == filter):
					inthere = True
		patente = f"{words} + {numbers}"
		if (inthere == False):
			return patente

	def generate(self, num: int):
		patentes = []

		for i in range(0, num):
			patente = self.calculate_patente()
			patentes.append(patente)
		return patentes
