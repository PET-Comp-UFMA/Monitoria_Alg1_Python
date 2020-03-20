"""

Faça um programa que receba um número e retorne o fatorial dele. O fatorial de
um número qualquer n é: n*(n-1)*(n-2)*(n-3)*....*1.

Exemplo:
        Entrada         Saída
        2        2*1    2
        3        3*2*1  6
        9               362880

"""

#Solução

num=int(input())
fact=1

for i in range(num, 0, -1):
    fact*=i
print(fact)