"""

Escreva um programa que receba inteiros até o usuário dar
entrada em um número negativo, e ao final mostre qual foi o
maior e o menor número recebido, bem como quantas vezes os 
mesmos foram inseridos.

Exemplo: Entrada        Saída
         1,2,3,4,4,1,-1 maior: 4, ocorreu 2 vezes
                        menor: 1, ocorreu 2 vezes

"""

numero = 0
maior = numero
menor= 0
contMenor = 0
contMaior = 0

while numero >= 0:
    print("Digite um número: ")
    numero=int(input())
    if menor ==0:
        menor=numero
    if numero > maior:
        maior=numero
        contMaior = 1
    elif numero == maior:
        contMaior=contMaior+1
    if numero>0:
        if numero<menor:
            menor=numero
            contMenor=1
        elif numero == menor:
            contMenor = contMenor+1

print("O maior número é "+ str(maior)+" e ocorreu "+ str(contMaior)+" vez(es)")
print("O menor número é "+ str(menor)+" e ocorreu "+ str(contMenor)+" vez(es)")

    
