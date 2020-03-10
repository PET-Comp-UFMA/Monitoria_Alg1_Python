def Primo(n):
    countDivision = 2
    if n%2 ==0 and n!=2:
        countDivision=countDivision+1
    elif n%3 == 0 and n!=3:
        countDivision= countDivision+1
    if countDivision>2:
        print("false")
    else:
        print("true")
    
n = int(input())

Primo(n)
