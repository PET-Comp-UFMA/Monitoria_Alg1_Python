print("Digite a quilometragem: ")
km = int(input())
print("Digite os litros ")
litros = int(input())

print(str(km/litros)+" km/l")

if km/litros > 14:
  print("É economico")

else:
  print("Não Economico")
  if km/litros <9:
    print("Sr.Anônio, melhor troca de carro ")

