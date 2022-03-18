# leia duas strings e imprima se a segunda string corresponde ao final da primeira string
# retorne true ou false
# Ex: rato  | to ; saida = true

string1 = input()
string2 = input()

print(string1[len(string2) * -1:] == string2)


