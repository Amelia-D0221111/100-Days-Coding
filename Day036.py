lstganjil = []
lstgenap = []

panjang = int(input("Masukkan Panjang: "))

for i in range(panjang):
	print("="*10)
	print(f"Iterasi ke-{i+1}")
	a = int(input("Masukkan Angka 1: "))
	b = int(input("Masukkan Angka 2: "))
	
	hasil = a + b
	print(f"Hasil: {hasil}")
	print("="*10)
	
	if (hasil % 2 == 0):
		lstgenap.append(hasil)
	else:
		lstganjil.append(hasil)
		
print(f"Genap: {lstgenap}")
print(f"Ganjil: {lstganjil}")