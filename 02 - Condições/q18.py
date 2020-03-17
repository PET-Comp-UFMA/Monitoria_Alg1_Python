"""
Você está em uma batalha pokemon e precisará entao calcular o dano que seus ataques causarão no adversário.
Os ataques levam em consideração 3 parâmetros, seu poder de ataque, a defesa inimiga e a efetividade do golpe.
A efetividade pode ser:
    Pouco efetiva: 0.5x
    Neutra: 1.0x
    Super efetiva: 2.0x
A efetividade é definida pelo tipo do seu pokemon e o tipo do inimigo, sendo eles grama, fogo e água
e a efetividade entre eles é:
    Grama > Água
    Água > Fogo
    Fogo > Grama
Caso sejam do mesmo tipo a efetividade será neutra.
Então, o programa a ser implementado deverá levar em consideração o ataque do seu pokemon, a defesa inimiga, 
o tipo do seu pokemon e o tipo inimigo. Sendo o dano calculado pela seguinte fórmula:
    dano = 50 * (ataque/defesa) * efetividade
Exemplo:
        Entrada: 100, 50, grama, água
        Saída: 200
        Entrada: 100, 100, água, fogo
        Saída: 25
        Entrada: 50, 25, água, água
        Saída: 100
"""

#Solução:

ataque, defesa, tipo_aliado, tipo_inimigo = int(input()), int(input()), str(input()), str(input())

if tipo_aliado=="grama" and tipo_inimigo=="fogo":
    efetividade=0.5
elif tipo_aliado=="grama" and tipo_inimigo=="agua":
    efetividade=2
elif tipo_aliado=="agua" and tipo_inimigo=="grama":
    efetividade=0.5
elif tipo_aliado=="agua" and tipo_inimigo=="fogo":
    efetividade=2
elif tipo_aliado=="fogo" and tipo_inimigo=="grama":
    efetividade=2
elif tipo_aliado=="fogo" and tipo_inimigo=="agua":
    efetividade=0.5
else:
    efetividade=1

dano = 50 * (ataque/defesa) * efetividade

print("O seu dano foi de: " + str(dano)) 
