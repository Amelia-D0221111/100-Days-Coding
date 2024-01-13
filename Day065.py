def operasi_set(set1, set2):
    gabungan = set1.union(set2)
    irisan = set1.intersection(set2)
   
    selisih_set1_set2 = set1.difference(set2)
    selisih_set2_set1 = set2.difference(set1)

    print(f'Gabungan: {gabungan}')
    print(f'Irisan: {irisan}')
    print(f'Selisih dari Set1 - Set2: {selisih_set1_set2}')
    print(f'Selisih dari Set2 - Set1: {selisih_set2_set1}')

set1 = {"apel", "jeruk", "pisang", "anggur","kelapa",}
set2 = {"jeruk", "anggur", "nanas", "melon","durian","kelapa"}

operasi_set(set1, set2)
