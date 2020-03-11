#Escreva uma função function ordenaVetor(v) que recebe um vetor de inteiros de tamanho 10,
#a função deve ordenar vetor de forma crescente.

import random

def organizaVetor(v):
    for i in range(1, len(v)-1):
        for j in range(0, len(v)-i):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    return v

vetor = []
for i in range(0, 10):
    vetor.append(random.randint(1,100))

print(vetor)
print(organizaVetor(vetor))
