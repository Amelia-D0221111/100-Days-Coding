def hitung_kemunculan_kata(teks):
    kata_dict = {}
    teks = teks.lower()
    kata_kunci = teks.split()
    for kata in kata_kunci:
        kata_dict[kata] = kata_dict.get(kata, 0) + 1

    for kata, jumlah in kata_dict.items():
        print(f'{kata}: {jumlah}')

teks_input = "Hi, saya amelia. saya berkuliah di universitas sulawesi barat."
hitung_kemunculan_kata(teks_input)
