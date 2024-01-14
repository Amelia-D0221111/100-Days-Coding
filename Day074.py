def ganti_vokal_dengan_at(string):
    string_hasil = ''.join('@'
     if char.lower() in 'aeiou'
     else char for char in string)
     
    return string_hasil

kalimat = "Selamat Sore, Bagaimana kabar mu hari ini"
kalimat_terganti = ganti_vokal_dengan_at(kalimat)

print(f"Kalimat setelah mengganti huruf vokal: {kalimat_terganti}")
