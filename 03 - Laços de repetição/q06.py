"""

Escreva um programa que receba 10 valores, e ao final,
imprima quantos valores negativos foram inseridos.

"""
cont = 0
print("Digite 10 valores")

for i in range(10):
    valor = int(input())
    if valor < 0:
        cont = cont + 1

print(str(cont) + " Números Negativos")
