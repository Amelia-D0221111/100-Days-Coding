def urutkan_berdasarkan_panjang(list_string):
    return sorted(list_string, key=len)

list_string = ["bersama" ,"kamu", "mereka","aku","siapa"]
hasil_urutan = urutkan_berdasarkan_panjang(list_string)
print(hasil_urutan)
