"""

Faca um programa que receba dois números com a mesma quantidade de digitos e mostre
a soma da distância entre os digitos do número. A distância entre os digitos é o valor
absoluto da diferença entre cada digito como no exemplo:
    Distancia entre os digitos de 234 e 489 -- |2 - 4| + |3 - 8| + |4 - 9| = 2 + 5 + 5 = 12

Exemplo
        Entrada         Saída
        121, 599        19
        20, 30          1
        10, 10          0

"""

#Solução

distância=0
num1=str(input())
num2=str(input())
l1=[]
l2=[]
l1.extend(num1)
l2.extend(num2)
for i in range(0,len(l1),1):
    distância+=abs(int(l1[i])-int(l2[i]))

print(distância)