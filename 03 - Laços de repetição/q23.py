"""

Escreva um programa que receba inteiros do usuário
até ele solicitar a parada e ao final mostre o maior
e o menor número recebido.

"""

continuar=True
maior=0
menor=0
cont=0
while continuar:
    num=int(input("Escreva o número: "))
    if cont==0:
        maior=num
        menor=num
    else:
        if maior<num:
            maior=num
        if menor>num:
            menor=num
    cont=int(input("Digite 1 para continuar ou 0 para parar: "))
    if cont==0:
        continuar=False
print("Maior: "+str(maior))
print("Menor: "+str(menor))