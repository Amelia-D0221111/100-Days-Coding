def hitung_jumlah_digit(angka):
    return len(str(abs(angka)))

angka_input = int(input("Masukkan angka: "))
jumlah_digit = hitung_jumlah_digit(angka_input)

print(f"Jumlah digit dalam angka tersebut: {jumlah_digit}")
