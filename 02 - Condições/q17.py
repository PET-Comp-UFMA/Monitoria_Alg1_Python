"""
Faça um programa que funcione como o teste de colisão entre dois retângulos.
Para cada um dos retângulos o programa deverá receber o seu ponto de origem (x e y), 
seu compriento em relação a x e sua altura em relação a y. O programa deverá então testar
se esses dois retângulos estão colidindo, ou seja se eles possuem algum ponto em comum,
tendo como saída true ou false.
Exemplo:
        Entrada: 0, 0, 30, 30
                 20, 20, 30, 30
        Saída: true
        Entrada: 0, 0, 50, 50
                 30, 30, 20, 20
        Saída: true
        Entrada: 0, 0, 20, 10
                 40, 40, 10, 10
        Saída: false
"""

#Solução:

x1, y1, l1, a1 = int(input()), int(input()), int(input()), int(input())
x2, y2, l2, a2 = int(input()), int(input()), int(input()), int(input())

if x1 <= x2+l2 and x2 <= x1+l1 and y1 <= y2+a2 and y2 <= y1+a1:
    print("true")
else:
    print("false")
