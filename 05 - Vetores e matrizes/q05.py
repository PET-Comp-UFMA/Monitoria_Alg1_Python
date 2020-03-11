#Faça uma função que receba um vetor de tamanho N com a altura de N pessoas na fila de uma padaria
#e retorna quantas podem ser vistas pelo padeiro. Use a seguinte assinatura: function visiveisFila(n)

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