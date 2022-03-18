def fatorial(n):
    if(n <= 1):
        return 1
    else:
        return n*fatorial(n-1)

n = int(input("Digite um numero: "))
print(str(fatorial(n)))
