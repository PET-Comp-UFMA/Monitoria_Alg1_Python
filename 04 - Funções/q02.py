#Questão 2
#Faça uma função que calcule a média das notas de um aluno. Ela deve ter a seguinte assinatura:
#function mediaAluno(nota1, nota2, nota3, tipoMedia)
#onde nota1, nota2 e nota3 são as notas do aluno, já tipoMedia é uma das seguintes médias: aritmética
#ou ponderada com pesos 2 4 e 2.

def mediaAluno(n1, n2, n3, tipoMedia):
    tipoMedia = tipoMedia.lower()
    if tipoMedia == "aritmetica":
        media = (n1+n2+n3)/3
    elif tipoMedia == "ponderada":
        media = (n1*2 + n2*4 + n3*2)/8
    return media

print(mediaAluno(7, 8, 9, "ponderada"))
    

