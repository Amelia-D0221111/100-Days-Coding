def hapus_karakter_non_alfabet(string):
    string_clean = ''.join(char for char in string if char.isalpha())
    return string_clean

kalimat = "amelia132018@gmail.com"

kalimat_bersih = hapus_karakter_non_alfabet(kalimat)

print(f"Kalimat setelah menghapus karakter non-alfabet: {kalimat_bersih}")
