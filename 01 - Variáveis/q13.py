total= int(input("Digite o numero total de eleitores: "))
validos = int(input("Digite o numero de votos validos: " ))
brancos = int(input("Digite o numero de votos brancos: " ))
nulos = int(input("Digite o numero de votos nulos: " ))

print("Validos: "+str(round((validos*100)/total,1))+"%")
print("Brancos: "+str(round((brancos*100)/total,1))+"%")
print("Nulos: "+str(round((nulos*100)/total,1))+"%")
