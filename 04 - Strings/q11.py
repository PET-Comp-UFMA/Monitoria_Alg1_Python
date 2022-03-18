# crie um programa que remova as silabas repitidas em uma frase:
# Ex: O papassarinho vovoou para bem longe == O passarinho voou para bem longe

string = input().split()
nova_string = ""
for palavra in string:
    if len(palavra) >= 4:
        if palavra[0:2] == palavra [2:4]:
            nova_string += palavra[2:]
        else:
            nova_string += palavra
    else:
        nova_string += palavra
    nova_string += " "
print(nova_string)
    