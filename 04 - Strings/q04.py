#Leia uma String e retorne na tela mostrando se é uma palíndroma.
#Um palíndromo é uma palavra ou frase que pode ser lida no seu sentido normal, da esquerda para a direita, bem como no sentido contrário, da direita para a esquerda, sem que haja mudança nas palavras que a formam e no seu significado.

palavra = input()
palavra = palavra.lower()
palavra = palavra.replace(" ", "")
palavraInvertida = palavra[::-1]

if palavra == palavraInvertida:
    print("Palíndromo")
else :
    print("Não Palíndromo")
