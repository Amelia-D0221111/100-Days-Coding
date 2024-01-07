def hitung_jumlah_kata(kalimat):
    kata_kata = kalimat.split()
    
    jumlah_kata = len(kata_kata)
    
    return jumlah_kata

kalimat_input = input("Masukkan kalimat: ")
jumlah_kata_hasil = hitung_jumlah_kata(kalimat_input)

print(f"Jumlah kata dalam kalimat: {jumlah_kata_hasil}")
