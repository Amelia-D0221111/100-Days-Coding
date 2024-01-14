def hitung_mean(data):
    if not data:
        return "List data kosong"
    
    total = 0
    jumlah_data = 0
    
    for nilai in data:
        total += nilai
        jumlah_data += 1
    
    mean = total / jumlah_data
    
    return mean

data = [2,1,6,7,5,9,3]
hasil_mean = hitung_mean(data)
print("Mean:", hasil_mean)
