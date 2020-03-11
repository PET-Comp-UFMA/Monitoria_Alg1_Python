#Dado um inteiro positivo N, faça um programa que gere os N primeiros números da seguinte
#sequência: 1², 2², 3², …, N².

numero = int(input("Digite um número: "))

for i in range(1, numero+1):
    print(pow(i, 2))
