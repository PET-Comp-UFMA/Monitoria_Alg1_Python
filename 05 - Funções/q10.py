def fibonacci(n):
    if (n <= 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci (n-2))
   
n = int(input("Digite a quantidade de numeros da sequencia: "))
for i in range(n):
    print(str(fibonacci(i)) + " ")
