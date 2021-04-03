# Crie um jogo que soma números aleatórios entre 1 e 100. Caso o usuário erre a conta o programa fecha.

import random

flag = True

while flag == True:
	a = random.randrange(1, 100)
	b = random.randrange(1, 100)	
	res = a+b
	respostaUser = int(input('Digite o resultado da soma de ' + str(a) + '+' + str(b) + ' '))
	if (res == respostaUser):
		flag = True
	else: 
		flag = False