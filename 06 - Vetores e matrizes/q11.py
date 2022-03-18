"""
Crie um programa que irá receber um número e uma quantidade e alocará em uma lista 
aquela quantidade de múltiplos do número.

Exemplo:
        Entrada     Saída
        5, 4        [5,10,15,20]
        2,10        [2,4,6,8,10,12,14,16,18,20]

"""

#Solução

num=int(input())
quantidade=int(input())
v=[]

for i in range(1,quantidade+1,1):
    v.append(num*i)
print(v)