"""

Faça um programa que receba 2 listas compostas por números inteiros e as junte em uma só
lista ordenada de forma não decrescente.

Exemplo
        Entrada             Saída
        [1,5,2,7],[3,2,9]   [1,2,2,3,5,7,9]
        [50,30,10],[15,10,5][5,10,10,15,30,50] 

"""

#Solução

l1=[52, 65, 26, 58, 84, 33, 37, 38, 85, 82]
l2=[59, 29, 85, 29, 41, 85, 55, 59, 31, 57]
tamanho=len(l1)+len(l2)
cont1=0
cont2=0
lmerge=[]

for j in range(1, len(l1), 1):
    for i in range(0, len(l1)-1, 1):
        if l1[i]>l1[i+1]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
for j in range(1, len(l2), 1):
    for i in range(0, len(l2)-1, 1):
        if l2[i]>l2[i+1]:
            l2[i],l2[i+1]=l2[i+1],l2[i]

print(l1)
print(l2)


for i in range(1, tamanho+1, 1):
    if cont1<len(l1) and cont2<len(l2):
        if l1[cont1]<=l2[cont2]:
            lmerge.append(l1[cont1])
            cont1+=1
        else:
            lmerge.append(l2[cont2])
            cont2+=1
    elif cont1>=len(l1):
        lmerge.append(l2[cont2])
        cont2+=1
    else:
        lmerge.append(l1[cont1])
        cont1+=1

print(lmerge)