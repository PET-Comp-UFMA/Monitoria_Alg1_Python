#Leia uma String, criptografe de acordo com a cifra de césar e mostre o resultado na tela.
#OBS: USE uma troca de 3 posições.
#É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes.

string = input()
novaString = ''
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in string:
    index = alfabeto.find(letra)
    index += 3
    if index > 25:
        index -= 25
    novaString += alfabeto[index]
print(novaString)
