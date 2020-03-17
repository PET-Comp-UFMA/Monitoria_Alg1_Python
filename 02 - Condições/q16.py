
"""
Crie um programa que avalie se a soma dos digitos de um número 
tem a mesma paridade que o número em si. O número deve conter apenas 3 digitos.
Exemplo:
		Entrada 						 	Saída
		123		1+2+3=6 par, 123 impar	 	false
		684		6+8+4=18 par, 684 par    	true
		353		3+5+3=11 impar, 353 impar	true
"""

#Solução:
import math
num = int(input())
digito1 = math.floor(num/100)
digito2 = math.floor(num/10)-digito1*10
digito3 = num-(digito1*100)-(digito2*10)
soma = digito1 + digito2 + digito3

if (soma%2) == (num%2):
	print("true")
else:
	print("false")
