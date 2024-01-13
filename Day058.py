def desimal_ke_biner(angka):
    if angka < 0:
        return "Angka harus non-negatif."
    elif angka == 0:
        return "0"
    else:
        biner = bin(angka)[2:]  
        return biner

angka_input = int(input("Masukkan angka desimal: "))
hasil_konversi = desimal_ke_biner(angka_input)

print(f"Hasil konversi ke biner: {hasil_konversi}")
