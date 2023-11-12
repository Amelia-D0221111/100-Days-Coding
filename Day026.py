genap = 0
ganjil = 0
lstgenap =[]
lstganjil = []

b = int(input("input angka->"))
for i in range(1, b + 1):
    if i % 2 == 0:
        lstgenap.append(i)
 
    else :
        lstganjil.append(i)
 
 
ganjil = sum(lstganjil)
genap = sum(lstgenap)
 
print(genap)
print(ganjil)