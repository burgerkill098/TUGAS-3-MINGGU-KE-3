daftar=input("masukkan list bilangan  :")
list_angka=daftar.split(',')
daftar_baru=[int(x) for x in list_angka]

jumlah= 0
for angka in daftar_baru:
    jumlah += angka 
rata_rata=jumlah/len(daftar_baru)

print("nilai rata rata {}".format(rata_rata))
print("jimlah total {}".format(jumlah))
print("nilai maksimum input :{}".format(max(daftar_baru)))
print("nilai minimal input :{}".format(min(daftar_baru)))
