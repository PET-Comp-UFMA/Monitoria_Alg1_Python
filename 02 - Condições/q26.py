num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))
num5 = int(input("Digite o quinto numero: "))

par = 0
impar = 0

if num1%2==0:
    par+=1
else:
    impar+=1

if num2%2==0:
    par+=1
else:
    impar+=1

if num3%2==0:
    par+=1
else:
    impar+=1

if num4%2==0:
    par+=1
else:
    impar+=1

if num5%2==0:
    par+=1
else:
    impar+=1

if par>impar:
    print("Maioria Par")
else:
    print("Maioria Impar")