def ganti_spasi_dengan_underscore(string):
    string_hasil = string.replace(" ", "_")
    return string_hasil

kalimat = "Amelia Unsulbar"

kalimat_terganti = ganti_spasi_dengan_underscore(kalimat)

print(f"Kalimat setelah mengganti spasi: {kalimat_terganti}")
