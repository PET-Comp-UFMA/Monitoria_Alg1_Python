# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa de imposto sobre o produto (MG 7%; SP %12; RJ 15%; MS 8%).
# Faça um programa em que o usuário entre com o valor e o estado de destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que 
# ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

print('Informe a sigla referente ao estado(Use maiúsculas)')
estado = str(input('Digite o estado '))
valorProduto = int(input('Valor de entrada: '))

if (estado.upper() == 'MG'):
	print('Estado selecionado: Minas Gerais')
	valorProduto += (valorProduto*0.07)
	print(valorProduto)
elif (estado.upper() == 'SP'):
	print('Esdado selecionado: São Paulo')
	valorProduto += (valorProduto*0.12)
	print(valorProduto)
elif (estado.upper() == 'RJ'):
	print('Esdado selecionado: Rio de Janeiro')
	valorProduto += (valorProduto*0.15)
	print(valorProduto)
elif (estado.upper() == 'MS'):
	print('Esdado selecionado: Mato Grosso do Sul')
	valorProduto += (valorProduto*0.08)
	print(valorProduto)