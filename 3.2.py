import fractions

u=int(input("SUKU DARI BERAPA :"))
un=int(input("SUKU AKHIR :"))
a=float(fractions.Fraction(input("ANGKA AWAL :")))
r=float(fractions.Fraction(input("RASIO :")))

hasil= 0
for n in range (u,un+1):
    suku=a*(r**(n-1))
    hasil=hasil +suku 
    print(suku)

print('jumlah semua suku (sn) =',hasil)