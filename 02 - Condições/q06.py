import random
import math

print("Digite o valor A: ")
a= int(input())
b= math.floor(random.uniform(2,20))
flag= True

if a%b==0 :
    print(str(flag))
else: 
    flag= False
    print(flag)

print(str(b))