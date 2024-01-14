def hitung_huruf_kapital(string):
    jumlah_kapital = sum(1 for char in string if char.isupper())
    return jumlah_kapital
    
kalimat = "Halo, Nama Saya AMELIA"
jumlah_kapital = hitung_huruf_kapital(kalimat)
print(f"Jumlah huruf kapital dalam kalimat: {jumlah_kapital}")
