"""
Maria e João vão a um evento mas só possuem 20 reais para os dois ingressos. 
A regra para o pagamento de ingressos é a seguinte: menores de 12 anos não pagam, 
pessoas de 12 anos a 17 anos pagam 10 reais; maiores de idade (18 anos ou mais) 
pagam 15 reais. Considerando que menores de 12 anos só entram no evento acompanhados 
de maiores de idade e que Maria e João só têm 20 reais para os ingressos, informe 
True caso ambos possam pagar e entrar no evento juntos ou False em caso contrário.
"""

#Solução

maria = int(input("Digite a idade de Maria: "))
joao = int(input("Digite a idade de João: "))

if (maria>18 or joao>18) and (joao<12 or maria<12):
    print(True)
elif (maria>12 and maria<17) and (joao>12 and joao<17):
    print(True)
else:
    print(False)
