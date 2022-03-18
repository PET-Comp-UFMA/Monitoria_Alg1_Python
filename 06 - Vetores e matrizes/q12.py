"""

Crie um programa que tenha como parâmetro uma lista de números inteiros
e remova dela todos os númros repetidos.

Exemplo:
        Entrada         Saída
        [1,2,1,3,4,2]   [3,4]
        [1,2,3,4,5,1]   [2,3,4,5]

"""

#Solução

v=[13,14,15,13,14,16,17,14,15,13,19]
posições=[]
for i in range(1,len(v),1):
    for j in range(0,len(v)-1,1):
        if v[j]>=v[j+1]:
            v[j],v[j+1]=v[j+1],v[j]


for i in range(0,len(v),1):
    if i<len(v)-1 and i>0:
        if v[i]==v[i-1] or v[i]==v[i+1]:
            posições.append(i)
    elif i==0:
        if v[i]==v[i+1]:
            posições.append(i)
    elif i==len(v):
        if v[i]==v[i-1]:
            posições.append(i)
contador=0
for i in posições:
    v.pop(i-contador)
    contador+=1

print(v)

