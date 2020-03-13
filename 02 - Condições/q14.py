#Questão 14
#Crie um algoritmo que receba os coeficientes a, b e c de uma equação do segundo grau e retorne a solução da equação.
#Caso a equação não tenha solução (delta menor que zero), informe isso ao usuário.

a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

delta = b*b-4*a*c

if delta < 0:
    print("A equação não tem solução.")
else:
    x1 = (-b + pow(delta, 1/2))/(2*a)
    x2 = (-b - pow(delta, 1/2))/(2*a)
    print("As raízes da equação são", x1, "e", x2)
