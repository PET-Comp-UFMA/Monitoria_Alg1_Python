import math

segundos = int(input("Digite o tempo em segundos: "))
horas = math.floor(segundos/3600)
segundos = segundos%3600
minutos = math.floor(segundos/60)
segundos = segundos % 60

print(str(horas)+":"+str(minutos)+":"+str(segundos))
