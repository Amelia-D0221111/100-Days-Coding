def jumlah_bilangan_bulat(daftar):
    if not daftar:  ''
        return 0
    else:
        angka_pertama = daftar[0]
        sisa_daftar = daftar[1:]
        if isinstance(angka_pertama, int):
            return angka_pertama + jumlah_bilangan_bulat(sisa_daftar)
        else:
            return jumlah_bilangan_bulat(sisa_daftar)
daftar_angka = [1, 2, 3, 4, 5, "6", "seven", 8]

hasil_jumlah = jumlah_bilangan_bulat(daftar_angka)

print(f"Jumlah bilangan bulat dalam daftar: {hasil_jumlah}")
