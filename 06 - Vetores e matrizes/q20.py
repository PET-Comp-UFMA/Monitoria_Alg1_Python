"""

Crie um programa que receba uma lista de inteiros e depois receba mais um inteiro f
após isso, mova todos os valores f da lista original para o final da lista.

Exemplo
Entrada                     Saída
[1, 2, 1, 4, 5, 1, 9], 1    [2, 4, 5, 9, 1, 1, 1]

"""

lista = []
index = 5
ocorrencias=0
cont = 0

for i in range(index):
    item = int(input("Digite o valor a ser adicionado na lista: "))
    lista.append(item)

final = int(input("Digite o valor a ser movido para o final: "))

while cont<index:
    if lista[cont]==final:
        lista.pop(cont)
        ocorrencias+=1
        cont-=1
        index-=1
    cont+=1


for i in range(ocorrencias):
    lista.append(final)

print(lista)