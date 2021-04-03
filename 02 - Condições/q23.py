# A nota final de um estudante é calculada a partir de três noas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laborátorio, 
# a uma avaliação semestral e um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; 
# Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está aprovado (média entre 0 e 2,9) de recuperação (entre 3 e 4,9) ou se foi aprovado.
# Faça todas as verificações necessárias.

notaLab = float(input('Nota trabalho laboratorio '))
notaAval = float(input('Nota avaliação semestral '))
notaExame = float(input('Nota exame final '))

notaLab = notaLab * 0.2
notaAval = notaAval * 0.3
notaExame = notaExame * 0.5

notaFinal = notaAval + notaExame + notaLab

print(notaFinal)

if 2.9 >= notaFinal >= 0:
	print('Reprovado')
elif 4.9 >= notaFinal >= 3:
	print('Recuperação')
elif notaFinal >= 5: 
	print('Aprovado')
else:
	print('Houve um erro')