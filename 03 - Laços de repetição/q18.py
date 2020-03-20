"""

Um número automórfico, é um número n que elevado a uma potência k resulta 
em outro número que tenha como seus ultimos dígitos o próprio número n.
    5^4 = 25 é automórfico pois 25 termina com 5
    5^3 = 125 é automórfico pois 12 termina com 5
    7^5 = 716807 é automórfico pois 716807 termina com 7
Um número pode ter várias potências que o faça ser automórfico. Faça um
programa que receba um número como entrada e verifique se ele é automórfico
em cada uma das potências de 2 a 10, e mostre para quais casos ele é.

"""

#Solução

import math
num=int(input())
digit=int(math.pow(10,len(str(num))))
for i in range(2, 11, 1):
    if (abs(math.pow(num,i))%digit)==num:
        print(i, end=" ")