"""

Faça um programa que receba uma string e imprima ela de volta com a formatação trocada,
ou seja, todas as letras que estiverem em minúsculo serão imprimidas em maiúsculo e todas
as letras em maiúsculo serão impressas em minúsculo.

Exemplo:
        Entrada     Saída
        Sino        sINO
        InVeJa      iNvEjA
        SABONETE    sabonete

"""

#Solução

string=str(input())
for i in string:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")

