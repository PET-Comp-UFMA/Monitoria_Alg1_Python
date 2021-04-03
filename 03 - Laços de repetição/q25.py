"""

Faça um programa que verifique se um número inserido pode 
ser resultado da soma de dois numeros primos. O programa 
deve receber um número, e fazer essa verificação, e se ela 
for verdadeira, ele deverá mostrar todas essas possibilidades.

Exemplo: Entrada Saída
         10      7 + 3
         16      3 + 13

"""
def eprimo(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

num = int(input("Informe o numero inteiro: "))
flag = False

for i in range(1, int(num/2+1)):
    par1 = i
    par2 = num-i

    if eprimo(par1) and eprimo(par2):
        print(str(par1)+" + "+str(par2))
        flag=True

if flag==False:
    print("O numero não pode ser resultado de nenhuma soma de primos.")


