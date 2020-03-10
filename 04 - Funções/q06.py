'''
Questão 6
Faça uma função que converta uma temperatura dada em Fahrenheit para Celsius ou Kelvin,
dependendo da conversão sinalizada.'''

def converteTemp(temperatura, escala):
    escala = escala.lower()
    if escala == "celsius":
        resultado = (temperatura - 32)/1.8
    elif escala == "kelvin":
        resultado = (5*temperatura - 160)/9 + 273.15
    return resultado

print(converteTemp(32, "Kelvin"))
print(converteTemp(32, "Celsius"))