def konversi_celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def konversi_fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

pilihan = input("Pilih konversi:\n1. Celsius ke Fahrenheit\n2. Fahrenheit ke Celsius\n")

if pilihan == '1':
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    hasil = konversi_celsius_ke_fahrenheit(celsius)
    print(f"Suhu dalam Fahrenheit: {hasil}°F")
elif pilihan == '2':
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    hasil = konversi_fahrenheit_ke_celsius(fahrenheit)
    print(f"Suhu dalam Celsius: {hasil}°C")
else:
    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
