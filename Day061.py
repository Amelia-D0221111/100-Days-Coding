def panjang_kata_terpanjang(kalimat):
    kata_kalimat = kalimat.split()
    panjang_kata = 0

    for kata in kata_kalimat:
        panjang_kata1 = len(kata)
        if panjang_kata1 > panjang_kata:
            panjang_kata = panjang_kata1

    return panjang_kata

kalimat = input("Masukkan kalimat: ")
hasil_panjang = panjang_kata_terpanjang(kalimat)

print(f"Panjang terpanjang dari kata-kata dalam kalimat tersebut: {hasil_panjang}")
