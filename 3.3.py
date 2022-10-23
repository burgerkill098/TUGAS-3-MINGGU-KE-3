n = int(input("Masukan Jumlah data = "))
bilangan = []

a = 0
b = 0
total = 0
while a < n:
    datainput = int(input("Masukan Nilai : "))
    bilangan.append(datainput)
    a += 1

while b < n:
    total = total + bilangan[b]
    b +=1

ratarata = total / n

print("total = ", total)
print("rata - rata = ", ratarata)

