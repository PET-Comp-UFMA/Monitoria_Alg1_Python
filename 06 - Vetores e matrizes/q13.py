"""

Crie um programa que receba um elemento (inteiro ou string) e mostre todos
os índices de ocorrencia desse parâmetro em uma lista.

Exemplo
        Entrada                     Saída
        [1,2,2,1,4,3], 2            [1,2]
        ["a","a","b","a"],"a"       [0,1,3]

"""

#Solução

v=["a","a","b","a","c"]
posições=[]
elemento=input()

for i in range(0,len(v),1):
    if v[i]==elemento:
        posições.append(i)
print(posições)
