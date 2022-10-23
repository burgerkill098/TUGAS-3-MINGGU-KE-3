from random  import randint

guesses=1
nomor =randint(1,10)

guess = int(input("TEBAK LAH ANGKA DARI 1 SAMPAI 10  :"))

while guess != nomor :
    if guess < nomor :
        print("TEBAKAN MU TERLALU RENDAH !!!!")
        guess=int(input(" TEBAK LAGI :"))
        guesses=guesses+1
    elif guess > nomor :
        print("TEBAKAN MU TERLALU BESAR !!!!")
        guess=int(input("TEBAK LAGI :"))
        guesses=guesses+1

print("SELAMAT JAWABAN MU  NOMOR YANG TEPAT !!!!!!!")

