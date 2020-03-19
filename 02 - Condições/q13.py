"""
Faça um programa que peça ao usuário que digite 3 números de 1 a 5 e então retorne
para ele quais números desse intervalo não foram digitados.

Exemplo:
        Entrada     Saída
        1, 2, 3     4, 5
        2, 3, 2     1, 4, 5
        1, 1, 1     2, 3, 4, 5
      
"""

#Solução

n1,n2,n3 = int(input()),int(input()),int(input())

if n1!=1 and n2!=1 and n3!=1 :
    print("1")
if n1!=2 and n2!=2 and n3!=2 :
    print("2")
if n1!=3 and n2!=3 and n3!=3 :
    print("3")
if n1!=4 and n2!=4 and n3!=4 :
    print("4")
if n1!=5 and n2!=5 and n3!=5 :
    print("5")
