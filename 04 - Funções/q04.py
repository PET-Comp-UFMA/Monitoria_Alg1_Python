def Maior(a,b):
    if a>b:
        return a
    else: 
        return b

def Menor(a,b):
    if a<b:
        return a
    else: 
        return b

def subtracaoMaiorMenor(a,b,c):
    high = Maior(a,Maior(b,c))
    low = Menor(b, Menor(a,c))
    return high-low

x,y,z = int(input()),int(input()),int(input())

print(subtracaoMaiorMenor(x,y,z))

