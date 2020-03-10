'''
Questão 1
Faça uma função que receba a altura (m), e o gênero de um(a) atleta (M ou F), e que retorne o peso
ideal (Kg) para esse indivíduo. Utilize as seguintes fórmulas:
Homens: (72.3 * h) - 58.2
Mulheres: (62.7 * h) - 45.2'''

def pesoIdeal(altura, genero):
    if genero == "m" or genero == "M":
        peso = (72.3 * altura) - 58.2
    elif genero == "f" or genero == "F":
        peso = (62.7 * altura) - 45.2
    return peso

print(pesoIdeal(1.7, "M"))