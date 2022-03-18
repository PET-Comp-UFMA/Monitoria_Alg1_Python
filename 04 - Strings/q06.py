# Crie um programa que receba uma string e substitua os numeros por letras de acordo com a tabela abaixo
# a = 1
# e = 2
# i = 3
# o = 4 
# u = 5
# ex: 1c4rd4

string = input()

string = string.replace('1', 'a');
string = string.replace('2', 'e');
string = string.replace('3', 'i');
string = string.replace('4', 'o');
string = string.replace('5', 'u');

print(string)