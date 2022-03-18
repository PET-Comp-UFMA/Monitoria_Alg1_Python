"""

Crie um programa que receba um vetor de strings e após isso receba uma outra
string e a insira no inicio de cada item da lista.

Exemplo
Entrada                 Saída
["a", "b", "c"] "al"    ["ala", "alb", "alc"]

"""

list = []
index = 3

for i in range(index):
    item = str(input("Digite o valor a ser adicionado na lista: "))
    list.append(item)

string = str(input("Digite a string a ser concatenada: "))

for i in range(index):
    list[i]=string+list[i]

print(list)