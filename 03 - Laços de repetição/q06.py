cont = 0
print("Digite 10 valores")

for i in range(9):
    valor = int(input())
    if valor < 0:
        cont = cont + 1

print(str(cont) + " Números Negativos")