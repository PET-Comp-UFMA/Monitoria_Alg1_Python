# crie um programa que some e ignore os zeros a direita do numero
# Ex: 15+5 é igual a 2 pois o 0 foi removido
# Ex: 99+6 = 15

num1 = int(input())
num2 = int(input())

soma = num1 + num2
soma = str(soma).replace("0", "")
print(soma)
