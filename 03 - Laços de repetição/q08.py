#Questão 8
#Crie um algoritmo que imprima todos os divisores de um número dado pelo usuário, com exceção do próprio número.

numero = int(input("Digite um número: "))

for i in range(1, numero):
    if numero%i == 0:
        print(i)