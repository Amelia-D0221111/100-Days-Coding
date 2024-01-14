def hapus_spasi(string):
    tanpa_spasi = string.replace(" ", "")
    return tanpa_spasi

kalimat = "saya Amelia angkatan 21"
hasil_tanpa_spasi = hapus_spasi(kalimat)
print(f"Kalimat setelah dihapus spasi: {hasil_tanpa_spasi}")
