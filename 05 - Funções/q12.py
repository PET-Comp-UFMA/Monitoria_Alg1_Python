"""

Faça uma função com três parâmetros: hora, minutos e segundos, dentro desta função, 
converta todos para segundos e apresente a soma dos três

"""

def segundos(h, m, s):
	sh = h * 3600
	sm = m * 60

	qtdS = sh + sm + s

	print(qtdS, 'segundos')

h = int(input())
m = int(input())
s = int(input())

segundos(h, m, s)
