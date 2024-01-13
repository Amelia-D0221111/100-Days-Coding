def gabung_dua_list(list1, list2):
    list_gabungan = sorted(list1 + list2)
    return list_gabungan

list1 = [3, 7, 1, 9, 4]
list2 = [5, 2, 8, 6]

list_terurut = gabung_dua_list(list1, list2)

print("List terurut setelah penggabungan:", list_terurut)
