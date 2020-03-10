'''
Questão 11
Faça um algoritmo que leia a idade de uma pessoa e imprima a seguinte mensagem, caso ela tenha
ao menos 18 anos: “Você é maior de idade”. Se a pessoa for menor de idade, imprima “Você é
menor de idade”.'''

idade = int(input("Digite a sua idade: "))
if idade < 17:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
