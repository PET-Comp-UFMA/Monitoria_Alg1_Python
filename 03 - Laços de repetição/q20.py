"""

Crie um programa que receba uma string, a construa, a desconstrua e imprima cada um desses passos.
Para entender melhor, observe o exemplo.

Exemplo:
        Entrada     Saída
        bola        b, bo, bol, bola, bol, bo, b
        HeLl        H, He, HeL, HeLl, HeL, He, H

"""

#Solução

string = str(input())
ajudante=""

for i in string:
    ajudante+=i
    print(ajudante)

for j in range(1, len(ajudante), 1):
    ajudante=ajudante[:-1]
    print(ajudante)