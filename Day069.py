def hitung_kemunculan_karakter(string, karakter):
    jumlah_kemunculan = string.count(karakter)
    return jumlah_kemunculan

kalimat = "hari ini hujan dan setiap hari hujan pada sore hari di mamuju"

karakter_yang_dicari = "hari"

jumlah_kemunculan = hitung_kemunculan_karakter (kalimat, karakter_yang_dicari)

print(f"Jumlah kemunculan karakter '{karakter_yang_dicari}' dalam kalimat: {jumlah_kemunculan}")
