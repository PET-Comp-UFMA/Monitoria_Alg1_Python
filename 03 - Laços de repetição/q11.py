"""

Faça um programa que retorne como sua saída uma pirâmide de asteriscos 
como a do exemplo a seguir:
    *
   ***
  *****
 *******
*********
O programa deverá receber uma entrada para que assim seja possível controlar o tamanho
da piramide que será impressa. Essa entrada pode ser tanto a altura em linhas da pirâmide
quanto o tamanho da base. Note que para a pirâmide ficar reta é necessário que o tamanho
de sua base e a quantidade de asteriscos em cada linha tem que ser ímpar.

Dica: Você pode começar fazendo o programa para imprimir a pirâmide de um tamanho específico
e sepois implementar a função de controlar o tamanho.

"""

#Solução

#Essa solução leva como parâmetro o tamanho em linhas da pirâmide

tamanho=int(input())
for i in range(1, tamanho+1, 1):
    for j in range(1, tamanho-i+1, 1):
        print(" ", end="")
    for k in range(1, (1+(i-1)*2)+1, 1):
        print("*", end="")
    print(" ")
    

    
