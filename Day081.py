def cek_pertama_dan_terakhir_sama(lst):
    if not lst:
        return "List kosong"
    
    return lst[0] == lst[-1]

data1 = [1, 2, 3, 4, 1]
data2 = [5, 6, 7, 8]

hasil1 = cek_pertama_dan_terakhir_sama(data1)
hasil2 = cek_pertama_dan_terakhir_sama(data2)

print(f"Hasil 1: {hasil1}")
print(f"Hasil 2: {hasil2}")
