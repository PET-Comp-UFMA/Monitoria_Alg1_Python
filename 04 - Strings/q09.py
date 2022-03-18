# Leia uma string e diga se é facil pronunciar ou nao
# Para ser uma palavra dificil de pronunciar deve possuir 3 consoantes seguidas
# Ex : Ferrari = Facil de pronunciar
# Ex : Hoffmann = Dificil de pronunciar
string = input()
vogais = 'aeiou'
consoantes_juntas = 0

for letra in string:
    if letra in vogais:
        consoantes_juntas = 0
    else:
        consoantes_juntas += 1

    if consoantes_juntas >= 3:
        break

if consoantes_juntas >= 3:
    print("Dificil de pronunciar")
else:
    print("Facil de pronunciar")