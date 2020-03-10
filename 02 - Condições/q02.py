#questao 2 -  condição
saldoInicial = float(input('Insira seu saldo inicial: '))
debitos = float(input('Insira o total de debitos: '))
creditos = float(input('Insira o total de creditos: '))

saldoFinal = saldoInicial + (creditos - debitos)

if saldoFinal > 0:
  print("Saldo porsitivo em R$",saldoFinal)
elif saldoFinal < 0:
  print("Saldo negativo em R$",-saldoFinal)
else:
  print("Saldo zero")

