#Questão 2
#Faça um programa que imprima o menor e o maior valor de um vetor com 100 números
#aleatórios.

import random

vetor = []

for i in range(0, 100):
    vetor.append(random.randint(1,1000))

menorNum = 1000
maiorNum = 1
for i in range(0, 100):
    if vetor[i] <= menorNum:
        menorNum = vetor[i]
    if vetor[i] >= maiorNum:
        maiorNum = vetor[i]

print("O menor número do vetor é", menorNum, "e o maior número do vetor é", maiorNum)