"""

Crie um programa que receba um valor de dinheiro em centavos e mostre como resultado
uma lista com a divisão desse valor da forma mais eficiente possível entre as moedas.
A lista deve ser preenchida seguindo o exemplo: 165 = ['100: 1', '50: 1', '25: 0', '10: 1', '5: 1']

"""

#Solução

num=int(input())
apoio=""
moedas=[100,50,25,10,5]
divisão=[]
for i in moedas:
    if num>=i:
        apoio=str(i)+": "+str(int(num/i))
        divisão.append(apoio)
        num=num%i
    else:
        apoio=str(i)+": "+str(0)
        divisão.append(apoio)

print(divisão)