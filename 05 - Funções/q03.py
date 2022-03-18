# -*- Coding: UTF-8 -*-
#coding: utf-8

"""
Faça uma função que receba as coordenadas de 4 pontos quaisquer no plano cartesiano e em
qualquer ordem, e retorne a área do quadrado formado por esses pontos. Caso não seja possível
formar um quadrado, imprima essa informação em tela. Desconsidere rotações do polígono (Os lados
do quadrado são paralelos aos eixos X e Y).
"""

import math
def squareArea(x1,y1,x2,y2,x3,y3,x4,y4):
    maiorX = x1
    if x2>maiorX :
        maiorX = x2
    elif x3>maiorX :
        maiorX = x3
    elif x4>maiorX :
        maiorX = x4

    menorX = x1
    if x2<menorX :
        menorX = x2
    elif x3<menorX :
        menorX = x3
    elif x4<menorX :
        menorX = x4

    maiorY = y1
    if y2>maiorY :
        maiorY = y2
    elif y3>maiorY :
        maiorY = y3
    elif y4>maiorY :
        maiorY = y4

    menorY = y1
    if y2<menorY :
        menorY = y2
    elif y3<menorY :
        menorY = y3
    elif y4<menorY :
        menorY = y4

    if maiorX-menorX != maiorY-menorY :
        print("Não formou um quadrado.")
    else:
        print(math.pow(maiorX-menorX,2))


x1 = input()
y1 = input()
x2 = input()
y2 = input()
x3 = input()
y3 = input()
x4 = input()
y4 = input()
squareArea(x1,y1,x2,y2,x3,y3,x4,y4)