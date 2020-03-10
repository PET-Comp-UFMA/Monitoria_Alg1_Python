import math
n = int(input())

if n>=0 and n<=10:
    print(n*n)
elif n < 0:
    print(-1*n)
else:
    print(math.sqrt(n))

