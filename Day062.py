def desimal_ke_romawi(angka):
    if not 0 < angka < 4000:
        return "Angka harus dalam rentang 1 hingga 3999."

    romawi_simbol = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    hasil_romawi = ""
    for nilai, simbol in romawi_simbol.items():
        while angka >= nilai:
            hasil_romawi += simbol
            angka -= nilai

    return hasil_romawi

angka_input = int(input("Masukkan angka desimal (1-3999): "))
hasil_romawi = desimal_ke_romawi(angka_input)

print(f"Hasil konversi ke Romawi: {hasil_romawi}")
