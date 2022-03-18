"""

Faça uma função que recebe dois catetos de um triangulo e calcule sua hipotenusa.

"""

import math

def hipotenusa(a, b):
	h = math.sqrt(pow(a,2) + pow(b, 2))

	print(h)

a = float(input('Cateto 1 '))
b = float(input('Cateto 2 '))

hipotenusa(a, b)
