import math 
numero = int(input())

numero1= math.floor(numero/1)%10
numero2 = math.floor(numero/10)%10
numero3 = math.floor(numero/100)%10
numero4 = math.floor(numero/1000)%10

print(str(numero1)+str(numero2)+str(numero3)+str(numero4))

