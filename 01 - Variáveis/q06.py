#Questão 6
#Dado uma variável A que receba qualquer informação de entrada do usuário, escreva um programa
#que imprima em tela o tipo de dado dessa variável, seguindo o formato: “O tipo da variável é TIPO.”,
#onde TIPO é um dos tipos de variáveis definidos na linguagem utilizada.
#(ex: em linguagens da família C, temos int, float, double, char, etc…, já em Lua, temos string,
#number, boolean, nil, etc...). Não use estruturas IF. Bibliotecas nativas são permitidas.

variavel = input('Digite a informação de entrada: ')
tipo = type(variavel)
print("A variável é do tipo", tipo)