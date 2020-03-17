"""
Faça um programa que receba valores para duas variáveis, podendo ser strings ou inteiros, e então
faça uma soma com esses valores de acordo com a seguinte condição:
    
    Se os dois valores forem strings, printe a soma deles como se eles fossem números inteiros,
    e se os dois valores forem inteiros, concatene-os como se fossem strings.
    Se os valores tiverem tipos diferentes, nada acontece.
O programa deverá perguntar ao usuário o tipo do valor antes de cada input. Mesmo que seja do tipo string,
o valor adicionado só poderá ser um numero.
Exemplo:
        Entrada     Saída
        "1", "2"    3
        1, 2        12
        "1", 2      -
"""

#Solução:

print("Digite 1 para inserir uma string e 2 para um inteiro: ")
tipo = int(input())
if tipo==1:
    print("Digite o primeiro valor")
    val1 = str(input())
elif tipo==2:
    print("Digite o primeiro valor")
    val1 = int(input())

print("Digite 1 para inserir uma string e 2 para um inteiro: ")
tipo = int(input())
if tipo==1:
    print("Digite o segundo valor")
    val2 = str(input())
elif tipo==2:
    print("Digite o segundo valor")
    val2 = int(input())

if type(val1)==type(val2):
    if type(val1)==int:
        print(str(val1)+str(val2))
    elif type(val1)==str:
        print(int(val1)+int(val2))
    else:
        print("-")
