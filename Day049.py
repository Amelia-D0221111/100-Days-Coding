def cari_nilai_maksimum(dictionary):
    if not dictionary:
        return None 
    maksimum = max(dictionary.values())
    return maksimum
data = {'a': 10, 'b': 5, 'c': 8, 'd': 12}
hasil = cari_nilai_maksimum(data)

print(f"Nilai maksimum dalam dictionary: {hasil}")
