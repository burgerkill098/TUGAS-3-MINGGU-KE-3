n= int(input("masukkan nilai N :"))
faktorial=1

for i in range (1,n+1):
    faktorial *=i

print(f'{n}! = {faktorial}')