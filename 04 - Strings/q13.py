# Escreva um programa que leia uma senha e diga se ela é valida ou nao
# Min 8 caracteres
# Possuir Letras Maiusculas e Minusculas
# Possuir Nin um numero
# Ex: 312Exemplo

string = input()

maiuscula = False
minuscula = False
numero = False

if len(string) >= 8:
    for x in string:
        if x.isupper():
            maiuscula=True
        if x.islower():
            minuscula=True
        if x.isalnum():
            numero = True
else:
    print("INVALIDA")
    
if maiuscula and minuscula and numero:
    print("VALIDA")
else:
    print("INVALIDA")
