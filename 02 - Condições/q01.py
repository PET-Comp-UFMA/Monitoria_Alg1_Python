altura = float(input('insira a sua altura: '))

peso = float(input('insira o seu peso: '))

imc = peso / (altura**2)

#print(imc)

if imc<=18:
  print('Abaixo do peso')
elif 25>imc>18:
  print('Peso Normal')
elif 30 > imc >= 25:
  print('Sobrepeso')
elif 40 > imc >= 30:
  print('Obeso Moderado')
else:
  print('Obeso morbido')