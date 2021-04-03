"""

Faça um programa que receba um número inteiro e mostre ao 
final a soma dos numeros pelos quais a entrada é divisível.

Exemplo: Entrada:10
         Saída: 8
         Pois o numero 10 pode ser dividido por 1, 2 e 5.

"""

numero = int(input("Digite um numero: "))
somaDivisao = 0
cont = 0

for i in range(1,int(numero/2+1)): 
    cont=cont+1
    if numero%cont == 0:   
        somaDivisao = somaDivisao + cont

print(str(somaDivisao+numero))
