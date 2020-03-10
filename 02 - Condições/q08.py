honda = 0
blanka = 0

print("Round 1")
entrance = input()
if entrance == "True":
    honda = honda + 1
    print("Honda")
else:
    blanka = blanka + 1
    print("Blanka")

print("Round 2")
entrance = input()

if entrance == "True":
    honda = honda + 1
    print("Honda")
else:
    blanka = blanka + 1
    print("Blanka")

if honda != 2 and blanka != 2:
    print("Final Round")
    entrance = input()
    if entrance == "True":
        print("O vencedor da luta é Honda!")
    else:
        print("O vencedor da luta é Blanka!")
else:
    if honda == 2:
        print("Vencedor é Honda!")        
    else:
        print("O vencedor é Blanka!")



