matriz = []
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input()))
    matriz.append(linha)

for i in range(3):
    for j in range(2):
        matriz[i].append(matriz[i][j])

somaPrim=0
j=0
for i in range(3):
    somaPrim = somaPrim + matriz[i][j]
    j= j+1
j=1
for i in range(3):
    somaPrim = somaPrim + matriz[i][j]
    j= j+1

somaSec = 0
j=4
for i in range(3):
    somaSec = somaSec + matriz[i][j]
    j= j-1
j=3
for i in range(3):
    somaSec = somaSec + matriz[i][j]
    j= j-1

print("A determinante é: ",somaPrim-somaSec)
