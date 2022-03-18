"""

Faça uma função que receba um vetor de tamanho N com a altura de N pessoas na fila de uma padaria
e retorna quantas podem ser vistas pelo padeiro. Use a seguinte assinatura: function visiveisFila(n).
Uma pessoa pode ser vista pelo padeiro se não houver nenhuma pessoa mais alta que ela em sua frente,
para entender melhor observe o exemplo.

Exemplo
Entrada                     Saída
[1.53, 1.70, 1.65, 1.80]    3
3 pessoas podem ser vistas, pois ele pode ver a posição 0, 1 e 3 da lista, mas não pode ver a 2, já
que ela é mais baixa que a posição 1.

"""
def visiveisFila(v):
    maisAlto = 0
    contador = 0
    for i in range(0, len(v)):
        if v[i] > maisAlto:
            maisAlto = vetor[i]
            contador += 1
    return contador

tamanhoFila = int(input("Digite quantas pessoas estão na fila: "))
vetor = []

for i in range(0, tamanhoFila):
    print("Digite a altura da", i+1, "ª pessoa na fila: ", end = '')
    vetor.append(float(input()))

pessoasVisiveis = visiveisFila(vetor)

print("O padeiro consegue ver", pessoasVisiveis, "pessoas na fila.")
