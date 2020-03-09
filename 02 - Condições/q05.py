import random
import math

print("Digite o valor A: ")
a= int(input())
b= math.floor(random.uniform(1,10))

if a<=10 and a>=0:
  if a%b==0:
    print(str(a)+" é divisível por "+str(b))
  else:
    print(str(a)+" não é divisível por "+ str(b))
    print("Resto: "+ str(a%b))

