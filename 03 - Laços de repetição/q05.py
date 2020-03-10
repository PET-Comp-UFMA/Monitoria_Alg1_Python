print("Digite um numero")
numero = int(input())
somaDivisao = 0
cont = 0

for i in range(1,int(numero/2)): 
    cont=cont+1
    if numero%cont == 0:   
        somaDivisao = somaDivisao + cont

print(str(somaDivisao))
