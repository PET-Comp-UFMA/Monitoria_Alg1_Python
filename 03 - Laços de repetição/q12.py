"""
Faça um programa que receba uma string e então mostre a primeira letra não repetida a aparecer.

Exemplo:
        Entrada     Saida
        "gato"      "g"
        "avaliação" "v"
        "arara"     "-"

"""

contador=0
string = str(input())
for x in string:
    for y in string:
        if x==y:
            contador+=1
    if contador<=1:
        print(x)
        break
    else:
        contador=0
