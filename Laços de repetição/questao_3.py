#Questão 2 - Número primo
#Classificação: Laços de repetição
#Dificuldade: fácil

#Crie um algoritmo que receba um número natural e informe se ele é ou não primo
#Um número primo é um número natural diferente de 1 que é divisível apenas por 1 e ele mesmo (Ex: 2, 3, 5, 7, 11, 13...)

numero = int(input("Digite um número natural: "))
flag = True
for i in range(2, numero):
    if numero%i == 0:
        print("O número", numero, "não é primo.")
        flag = False
        break

if flag:
    print("O número", numero, "é primo.")