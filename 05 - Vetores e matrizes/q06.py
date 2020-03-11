#Faça um programa que receba do usurário 10 números. O programa deverá calcular a
#quantidade de elementos pares e imprimir cada elemento. Deverá também calcular e exibir a
#soma de todos esses elementos. Caso nenhum dos elementos sejam pares, exiba a seguinte
#mensagem: "Não há elementos pares".

vetor = []
for i in range(0, 10):
    vetor.append(int(input("Digite um número: ")))

contador = 0
somaPar = 0

for i in range(0, 10):
    if vetor[i]%2 == 0:
        contador += 1
        somaPar += vetor[i]

if contador == 0:
    print("Não há elementos pares.")
else:
    print("Existem", contador, "números pares no vetor e a soma de todos eles é igual a", somaPar)
