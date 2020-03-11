#Questão 8
#Faça um programa que receba como entrada um número real qualquer, e que imprima em tela um
#número inteiro maior ou igual à entrada, usando a função teto. Caso o número seja negativo, ele deve
#ser tratado como número positivo. Não utilize estruturas IF.

import math

numero = float(input("Digite um número real: "))
numero = abs(numero)
numero = math.ceil(numero)
print(numero)
