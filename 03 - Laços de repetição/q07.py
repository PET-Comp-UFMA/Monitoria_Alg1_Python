"""

Faça um programa que receba um inteiro positivo e imprima a seguinte sequência
de asteriscos de acordo com o numero recebido.

Exemplo:  

Entrada: 5  
Saída:
*
* *
* * *
* * * *
* * * * *

Entrada: 9
saída:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *

"""
linhas = int(input("Digite o numero de linhas do padrão: "))
for i in range(linhas):
    for j in range(linhas):
        if i >= j:
            print("* ", end="")#o parâmetro 'end=""' faz com que não haja quebra de linha
        else:   
            print(" ", end="")    
    print("")
