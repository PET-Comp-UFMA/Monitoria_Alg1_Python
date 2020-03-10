scorpion = 0
subzero = 0

print("Round 1")
entrance = input()
if entrance == "true":
    scorpion = scorpion + 1
    print("Scorpion")
elif entrance == "false":
    subzero = subzero + 1
    print("Subzero")
else: 
    print("Toasty!!")    
    

print("Round 2")
entrance = input()
if entrance == "true":
    scorpion = scorpion + 1
    print("Scorpion")
elif entrance == "false":
    subzero = subzero + 1
    print("Subzero")
else: 
    print("Toasty!!")    
    

print("Round 3")
entrance = input()
if entrance == "true":
    scorpion = scorpion + 1
    print("Scorpion")
elif entrance == "false":
    subzero = subzero + 1
    print("Subzero")
else: 
    print("Toasty!!")    
    

if scorpion != 3 and subzero !=3:
    print("Round 4")
    entrance = input()
    if entrance == "true":
        scorpion = scorpion + 1
        print("Scorpion")
    elif entrance == "false":
        subzero = subzero + 1    
        print("Subzero")
    else: 
        print("Toasty")    
        

    if scorpion != 3 and subzero != 3 :
        print("Final Round")
        entrance = input()
        if entrance == "true" :
            print("O vencedor da luta é Scorpion!")
        elif entrance == "false" :
            print("O vencedor da luta é Subzero!")
        else:
            print("Toasty!!!")
        

    else:
        if scorpion == 3:
            print("O vencedor da luta é Scorpion!")
        else:
            print("O vencedor da luta é Subzero!")


else:
    if scorpion == 3:
        print("O vencedor da luta é Scorpion!")
    else:
        print("O vencedor da luta é Subzero!")





