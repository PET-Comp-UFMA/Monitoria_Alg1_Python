def permuta(a,b,c): 
    temp = a
    a = b
    b = temp
    print("A = " + str(a) + ", B = " + str(b) + ",C = " + str(c))
x = input()
y = input()    
z = input()
permuta(x,y,z)
permuta(y,z,x)
permuta(x,y,z)
permuta(x,z,y)
