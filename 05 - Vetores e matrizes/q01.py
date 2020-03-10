'''
Questão 1
Escreva um programa que altere todos os valores de um vetor de tamanho N preenchido com
números aleatórios de 1 a 20, se o valor for ímpar deve se multiplicar por 3, se for par
deve-se subtrair 1 e multiplicar por 2. no final imprima o vetor antes e depois das alterações
serem feitas.'''

import random

vetor = []

for i in range(0, 10):
    vetor.append(random.randint(1,20))

print(vetor)

for i in range(len(vetor)):
    if vetor[i]%2 != 0:
        vetor[i] = vetor[i]*3
    else:
        vetor[i] = (vetor[i] - 1) * 2

print(vetor)





