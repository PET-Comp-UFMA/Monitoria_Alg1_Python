"""

Faça um programa que mostre o resultado de uma potenciação sem a utilização da biblioteca
math. O programa deverá receber como entrada a base e o expoente da potenciação, e calcular
o resultado utilizando um loop.

Exemplo:
        Entrada     Saída
        2,2         4
        3,3         27
        2,10        1024

"""

#Solução

num=int(input())
exp=int(input())
resposta=num
for i in range(1, exp, 1):
    resposta*=num
print(resposta)