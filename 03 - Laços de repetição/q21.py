"""

A sequência de Fribonacci é uma sucessão de números que começa por
1 e 0 e o número seguinte será sempre a soma dos dois anteriores.
Escreva um programa que receba um numero n inteiro e maior ou igual a 2
e imprima na tela os n primeiro termos da sequência de Fribonacci.

Exemplo: Entrada   Saída
         5         0, 1, 1, 2, 3
         10        0, 1, 1, 2, 3, 5, 8, 13, 21, 34

"""
n1=0
n2=1
prox=0
cont=0
n = int(input("Escreva a quantidade de numeros a serem impressos (minimo 2): "))
while n<2:
    print("Número inválido, a quantidade mínima tem que ser 2.")
    n = input("Escreva a quantidade de numeros a serem impressos (minimo 2): ")
while cont<n:
    if cont==0:
        print(n1, end='')
    else:
        print(", "+str(n2), end='')
        prox=n1+n2
        n1=n2
        n2=prox
    cont+=1    