"""

Crie um programa que receba um número e informe se esse número está presente
em uma lista.

Exemplo:
        Entrada         Saída
        [1,2,3,4,5], 5  true
        [1,2,3], 10     false
        [100,90,80], 80 true

"""

#Solução

import random

random.seed(1)

v=[]
for i in range(1, 100, 1):
    v.append(random.randint(1,1000))

num = int(input())

for i in v:
    if i==num:
        print("true")
        break