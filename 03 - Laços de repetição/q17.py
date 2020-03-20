"""

Faça um programa que recema um número em binário e então o converta para decimal.

Exemplo:
        Entrada     Saída
        110         6
        10          4
        11111111    255

"""

#Solução

import math
binary=str(input())
cont=len(binary)-1
num=0

for i in binary:
    j=int(i)
    if j==1:
        num+=math.pow(2,cont)
    cont-=1
print(int(num))