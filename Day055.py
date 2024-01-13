def hitung_kata(teks):
    kata = teks.split()
    jumlah = set(kata)
    return len(jumlah)

teks = input("Masukkan teks: ")
jumlah_kata = hitung_kata(teks)

print(f"Jumlah kata dalam teks tersebut: {jumlah_kata}")
