#Leia uma String e retorne quantas vogais ela possui na tela.
palavra = input()
contador=0
for letra in palavra:
    if letra in 'aeiou':
        contador += 1
print(contador)
