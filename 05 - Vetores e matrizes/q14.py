"""

Faca um rograma que verifique se o utimo elemento de uma lista é uma 
combinação dos outros elementos em ordem.

Exemplo:
        Entrada                         Saída
        [1,2,3,"123"]                   true
        [1,53,4,"1543"]                 false
        ["sanc","tuary","sanctuary"]    true

"""

#Solução

v=["san","ctu","ary","sanctuar"]
match=""

for i in range(0,len(v)-1,1):
    match+=str(v[i])

if match==v[len(v)-1]:
    print("true")
else:
    print("false, o elemento deveria ser: ",match)