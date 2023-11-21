awal = int(input("Awal : "))
akhir = int(input("Akhir : "))

genap = []
ganjil = []
if awal < akhir:
    for i in range(awal,akhir+1):
        if i % 2 == 0:
            genap.append(i)
        else:
            ganjil.append(i)
else:
    for i in range(akhir,awal+1):
        if i % 2 == 0:
            genap.append(i)
        else:
            ganjil.append(i)
print(f"Genap : {genap}")
print(f"Ganjil : {ganjil}")

hasil_genap = genap[0]
hasil_ganjil = ganjil[0]
for i in range(1,len(genap)):
    hasil_genap -= genap[i]
for i in range(1,len(ganjil)):
    hasil_ganjil -= ganjil[i]

print(f"Genap : {hasil_genap}")
print(f"Ganjil : {hasil_ganjil}")
