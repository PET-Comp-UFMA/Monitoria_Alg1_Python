#Questão 9
#Crie um algoritmo que printe a soma de todos os números pares e a soma de todos os números ímpares de um intervalo dado pelo usuário.

somaPar, somaImpar = 0, 0
minimo = int(input("Digite o primeiro número do intervalo: "))
maximo = int(input("Digite o último número do intervalo: "))

for i in range(minimo, maximo):
    if i%2 == 0:
        somaPar = somaPar + i
    else:
        somaImpar = somaImpar + i

print("A soma de todos os pares no intervalo dado é ", somaPar)
print("A soma de todos os ímpares no intervalo dado é ", somaImpar)