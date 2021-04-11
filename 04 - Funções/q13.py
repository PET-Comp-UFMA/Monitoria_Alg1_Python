"""

Faça uma função que recebe dois números inteiros e retorna a soma dos números entre eles

Exemplo
Entrada   Saída
1 e 5     2 + 3 + 4 = 9

"""
def somaEntre(n1, n2):
	soma = 0
	for i in range (n1+1, n2):
		print(i)
		soma += i
	
	print(soma)

n1 = int(input('Primeiro valor '))
n2 = int(input('Segundo valor '))

somaEntre(n1, n2)
