for i in range(9):
    for j in range(9):
        if i >= j:
            print("* ", end="")#o parâmetro 'end=""' faz com que não haja quebra de linha
        else:   
            print(" ", end="")    
    print("")
