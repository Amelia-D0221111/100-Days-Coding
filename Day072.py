def ganti_huruf_kecil_dengan_bintang(string):
    string_hasil = ''.join('*' if char.islower() else char for char in string)
    return string_hasil

kalimat = "Halo, Bagaimana kabar mu hari ini"

kalimat_terganti = ganti_huruf_kecil_dengan_bintang(kalimat)

print(f"Kalimat setelah mengganti huruf kecil: {kalimat_terganti}")
