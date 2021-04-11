"""

Faça um programa que receba um vetor com 4 indices e imprima um novo vetor 
com todas as subvetores do vetor original.

Exemplo:
Entrada         Saída
[1, 2, 3, 4]    [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

"""

list = []
sublists = []
index = 4

for i in range(index):
    item = int(input("Digite o valor a ser adicionado na lista"))
    list.append(item)

for i in range(4):
    sublists.append([list[i]])

for i in range(0, 3):
    for j in range(i+1, 4):
        sublists.append([list[i],list[j]])

for i in range(0, 2):
    for j in range(i+1, 4):
        for k in range(j+1, 4):
            sublists.append([list[i],list[j],list[k]])
sublists.append([list[0],list[1],list[2], list[3]])

print(sublists)