"""
Crie um programa que cheque se o número digitado é simétrico
Exemplo:
		Entrada 	Saída
		123     	False
		121     	True
		23432   	True
"""
#Solução:
print("Digite um número: ")
num= str(input())
if num == num[::-1]:
	print("true")
else:
	print("false")
