"""

Faça um programa que receba uma string e retorne ela removendo todas as letras consecultivas
iguais.

Exemplo:
        Entrada     Saída
        bboollaa    bola
        carro       caro
        ccccccãaoo  cãao

"""

#Solução

comparador="that's not a letter"
string = str(input())
for i in string:
    if i!=comparador:
        print(i, end="")
    comparador=i