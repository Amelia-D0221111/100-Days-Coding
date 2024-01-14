def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Pembagian dengan nol tidak dapat dilakukan"
    return a / b

hasil_penjumlahan = penjumlahan(2, 2)
hasil_pengurangan = pengurangan(5, 3)
hasil_perkalian = perkalian(4, 6)
hasil_pembagian = pembagian(8, 2)

print(f"Penjumlahan: {hasil_penjumlahan}")
print(f"Pengurangan: {hasil_pengurangan}")
print(f"Perkalian: {hasil_perkalian}")
print(f"Pembagian: {hasil_pembagian}")
