def tempAposentadoria(idade, tempoTrabalho):
    if idade>= 65 and tempoTrabalho >=30:
        return True
    else: 
        return False

def aposentadoria2019(trabalhador, nasc, anoIngresso):
    if tempAposentadoria(2019-nasc, 2019-anoIngresso) == True:
        print(trabalhador + " tem aposentadoria em 2019")
    else:
        print(trabalhador + " não tem aposentadoria em 2019")    
        print("Trabalhe mais " + str(30-(2019-anoIngresso)) + " anos.")
        if 2019-nasc<65:
            print("Muito novo para se aposentar.")

trabalhador = input()
anoNasc = int(input())
anoIngresso = int(input())
aposentadoria2019(trabalhador, anoNasc, anoIngresso)