def tempAposentadoria(idade, tempoTrabalho):
    if idade >= 65 and tempoTrabalho >= 30:
        return True
    else:
        return False

idade = int(input())
tempoTrabalho = int(input())

print(tempAposentadoria(idade,tempoTrabalho))