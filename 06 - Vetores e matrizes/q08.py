"""

Faça um programa que receba uma matriz de ordem n e depois a imprima na tela,
seguida de sua transposta, sua diagonal principal e seu triângulo superior.

Exemplo:
Entrada:    Saída
1 2 3       1 2 3   1 4 7   1    2 3
4 5 6       4 5 6   2 5 8    5     6
7 8 9       7 8 9   3 6 9     9

"""

import random

random.seed(1)
ordem = int(input("Qual a ordem da matriz gerada? "))

matriz=[]
for i in range(ordem):
    linha=[]
    for j in range(ordem):
        linha.append(random.randint(1,9))
    matriz.append(linha)

print("\nA matrz gerada:")
for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], end="\t")
    print("")

print("\nA matrz transposta:")
for i in range(ordem):
    for j in range(ordem):
        print(matriz[j][i], end="\t")
    print("")

j=0
esp=""
print("Diagonal principal:",end="\n")
for i in range(ordem):
    print(esp,matriz[i][j], end="\n")
    for u in range(i+1):
        esp="\t"*(i+1)
    j+=1

print("Triangulo superior:",end="\n")
for i in range(ordem):
    for j in range(ordem):
        if j<=i: print("\t",end="")
        else: print("\t",matriz[i][j],end="")
    print("\n")    

print(matriz)
