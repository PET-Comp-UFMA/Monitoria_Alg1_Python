"""

Crie um programa que verifique se em uma lista preenchida por inteiros
seus componentes podem ser organizados para formar uma lista de números
consecultivos e sem repetições.

"""

#Solução

v=[0,2,5,4,3,1,6,8,7]
flag=False
for i in range(1,len(v),1):
    for j in range(0,len(v)-1,1):
        if v[j]>=v[j+1]:
            v[j],v[j+1]=v[j+1],v[j]

for i in range(0,len(v)-1,1):
    if v[i+1]-v[i]==1:
        flag=True
    else:
        flag=False
        break

print(flag)