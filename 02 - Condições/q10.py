'''
Questão 10
Dado os três lados de um triângulo, faça um programa que indique se esse triângulo é equilátero,
isósceles ou escaleno.
OBS: Observe que os lados só formam um triângulo se o comprimento de cada lado for sempre menor
que a soma dos outros dois lados.(Exiba uma mensagem de erro, caso o critério não seja satisfeito).'''

lado1 = int(input("Digite a medida do primeiro lado: "))
lado2 = int(input("Digite a medida do segundo lado: "))
lado3 = int(input("Digite a medida do terceiro lado: "))

if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print("Não é possível formar um triângulo com as medidas dadas.")
else:
    if lado1 == lado2 and lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3 :
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")