"""

Faça uma função que receba a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
calcule o consumo em Km/l e escreva mensagns de acordo com o resultado do consumo

"""

def calcConsumo(Km, L):
	consumo = Km / L

	if consumo < 8:
		print("Consumo alto")
	elif consumo >= 8 and consumo <= 12:
		print("Consumo regular, seu carro pode ser considerado econômico")
	elif consumo > 12:
		print("Consumo super ecônomico")


Km = float(input('Digite a quantida de km rodados: '))
L = float(input('Digite a quanidade de litros consumidos: '))
calcConsumo(Km, L)
