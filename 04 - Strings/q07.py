# crie um programa que receba uma string e deixe a primeira letra de cada palavra em maiuscula

# ex : lorem ipsum
string = input().split()
nova_string = "";
for n in string:
    nova_string += " "
    nova_string += n.capitalize()
print(nova_string)
