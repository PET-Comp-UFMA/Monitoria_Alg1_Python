#Questão 10
#Faça um código que peça um número natural N ao usuário e printe um triângulo de
#asteriscos de N linhas na tela. Exemplo: 
#N = 5
#*
#**
#***
#****
#*****

n = int(input("Digite um número natural: "))

for i in range(n):
    for j in range(i+1):
        print("*", end = "")
    print("")