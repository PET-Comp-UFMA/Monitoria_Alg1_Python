#Dado um inteiro positivo N, faça um programa que gere os próximos N números da seguinte
#sequência: 1², 2², 3², …, N², a partir do N-ésimo termo.

numero = int(input("Digite um número: "))

for i in range(numero, numero+numero):
    print(pow(i, 2))