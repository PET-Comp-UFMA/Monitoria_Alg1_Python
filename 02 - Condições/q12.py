"""
Faça um programa que peça ao usuário 3 números e então retorne quais desses números é o maior.

Exemplo:
        Entrada     Saída
        1, 2, 3     3
        12, 45, 11  45
        -3, -1, -50 -1
        
"""

#Solução

n1, n2, n3 = int(input()),int(input()),int(input())

if n1>n2 and n1>n3 :
    print(str(n1)+" é o maior")
elif n2>n1 and n2>n3 :
    print(str(n2)+" é o maior")
else:
    print(str(n3)+" é o maior")
