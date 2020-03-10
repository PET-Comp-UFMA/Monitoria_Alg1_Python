print("Informe a idade em anos, meses e dias.")
anos = int(input())
meses = int(input())
dias = int(input())
total = dias

total = total + (anos*365) + (meses*30)

print(str(total) + " dias")