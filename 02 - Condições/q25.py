num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))
num5 = int(input("Digite o quinto numero: "))
num6 = int(input("Digite o sexto numero: "))
num7 = int(input("Digite o setimo numero: "))

primeiro = num1
segundo = num2
terceiro = num3

def maior(num,primeiro,segundo,terceiro):
    if num>primeiro:
        primeiro,segundo,terceiro = num,primeiro,segundo
    elif num>segundo:
        segundo,terceiro = num,segundo
    elif num>terceiro:
        terceiro=num
    return primeiro, segundo, terceiro

primeiro,segundo,terceiro=maior(num2,primeiro,segundo,terceiro)
primeiro,segundo,terceiro=maior(num3,primeiro,segundo,terceiro)
primeiro,segundo,terceiro=maior(num4,primeiro,segundo,terceiro)
primeiro,segundo,terceiro=maior(num5,primeiro,segundo,terceiro)
primeiro,segundo,terceiro=maior(num6,primeiro,segundo,terceiro)
primeiro,segundo,terceiro=maior(num7,primeiro,segundo,terceiro)

print(terceiro)

"""if segundo>primeiro:
    segundo,primeiro = primeiro,segundo
if terceiro>primeiro:
    terceiro,primeiro = primeiro,terceiro

if num4>primeiro:
    primeiro,segundo,terceiro = num4,primeiro,segundo
elif num4>segundo:
    segundo,terceiro = num4,segundo
elif num4>terceiro:
    terceiro=num4

if num5>primeiro:
    primeiro,segundo,terceiro = num5,primeiro,segundo
elif num5>segundo:
    segundo,terceiro = num5,segundo
elif num5>terceiro:
    terceiro=num5

if num6>primeiro:
    primeiro,segundo,terceiro = num6,primeiro,segundo
elif num6>segundo:
    segundo,terceiro = num6,segundo
elif num6>terceiro:
    terceiro=num6

if num7>primeiro:
    primeiro,segundo,terceiro = num7,primeiro,segundo
elif num7>segundo:
    segundo,terceiro = num7,segundo
elif num7>terceiro:
    terceiro=num7"""
