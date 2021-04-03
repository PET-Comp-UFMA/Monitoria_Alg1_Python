"""

Os números de armstrong são números que a soma total dos
cubos de cada um de seus dígitos é igual ao proprio número.

Exemplo: 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153

Faça um programa que imprima todos os números de armstrong
que se encontram entre 1 e 500.

"""


for i in range(1,501):
    temp=i

    digito1=temp%10
    temp=int(temp/10)
    
    digito2=temp%10
    temp=int(temp/10)
    
    digito3=temp%10

    if ((digito1*digito1*digito1) + (digito2*digito2*digito2) + (digito3*digito3*digito3))==i:
        print(i)
