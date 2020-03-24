"""
Crie um programa que receba 3 valores, compare-os e printe ao final o número de valores iguais.

Exemplo: 
        Entrada     Saída
        1, 2, 3     0
        2, 3, 2     2
        7, 7, 7     3

"""

#Solução

contador=0
num1, num2, num3 = int(input()), int(input()), int(input())
if num1==num2:
    contador+=1
if num2==num3:
    contador+=1
if num1==num3:
    contador+=1

print("A quantidade de números iguais é: " + str(contador))
