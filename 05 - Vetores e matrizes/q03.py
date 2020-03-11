#Questão 3
#Faça um algoritmo para ler um vetor de 30 números. Após isto, receba mais um número N
#qualquer, para calcular quantas vezes esse número aparece no vetor.'''

import random

vetor = []

for i in range(0, 30):
    vetor.append(random.randint(1,100))
    print(vetor[i])

numero = int(input("Digite um número: "))
contador = 0

for i in range(0, 30):
    if vetor[i] == numero:
        contador += 1

print("O número aparece", contador, "vezes no vetor.")