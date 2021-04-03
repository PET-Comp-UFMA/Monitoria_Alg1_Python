"""

Faça um programa que receba um inteiro e imprima
um padrão como o do exemplo, para qualquer número
de 1 a 9.

Exemplo: Entrada  Saída
            5       1
                   2 2
                  3 3 3
                 4 4 4 4
                5 5 5 5 5


            9           1
                       2 2
                      3 3 3
                     4 4 4 4
                    5 5 5 5 5
                   6 6 6 6 6 6
                  7 7 7 7 7 7 7
                 8 8 8 8 8 8 8 8
                9 9 9 9 9 9 9 9 9

"""

num = int(input("Informe um inteiro de 1 a 9 para formar o padrão: "))

for i in range(1, num+1):
    for j in range(num-i, 0, -1):
        print(" ", end='')
    for k in range(1, i*2):
        if k%2==1:
            print(i, end='')
        else:
            print(" ", end='')
    print("")