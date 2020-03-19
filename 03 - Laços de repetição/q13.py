"""
Faça um programa que funcione como uma loja. Esse programa deverá mostrar os itens
que estão a venda e o preço de cada um e então receberá como entrada o item a ser
comprado e a quantidade, ele deverá então perguntar se o usuário deseja continuar 
comprando ou encerrar a compra. Ao final, o programa deverá mostrar quanto será o 
total a ser pago pelo usuário.

Exemplo:
        Entrada         Saída
                        O que desea comprar?
        item 1 Qtd:5    Deseja continuar?
        sim             O que deseja comprar?
        item 2 Qtd:5    Deseja continuar?
        não             Sua conta foi de xxx gold.

"""

#Solução

x=1
carrinho=0
print("1- Poção de vida:             50g")
print("2- Éter:                     100g")
print("3- Elixir:                   500g")
print("4- Antídoto:                  75g")
while x!=0:
    item=int(input("O que você gostaria de comprar? "))
    quantidade=int(input("Quantos você gostaria? "))
    if item==1:
        carrinho+=quantidade*50
    elif item==2:
        carrinho+=quantidade*100
    elif item==3:
        carrinho+=quantidade*500
    elif item==4:
        carrinho+=quantidade*75
    x=int(input("Você gostaria de continuar comprando? Digite 0 para encerrar a compra e qualquer outra coisa para continuar: "))
print("O total da sua compra foi de: "+ str(carrinho) + "g.")

