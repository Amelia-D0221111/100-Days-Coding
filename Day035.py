print("Menghitung Indeks Massa Tubuh ")
print("__________________________________")
bb = float(input("Masukkan Berat Badan : "))
tb = float(input("Masukkan Tinggi Badan : "))
tb /= 100 # cm ke meter
rumus = bb / (tb**2)
rumus = round(rumus, 2) #pembulatan

print("Indeks Massa Tubuh anda : " , rumus)