
x=int(input("X   :"))
y=int(input("Y   :"))

jumlah = 0

print("Deret = ", end="") 
while x + 1 < y:
    x = x + 1
    jumlah = jumlah + x 
    print(x, end=" ")
print("\njumlah = ", jumlah)