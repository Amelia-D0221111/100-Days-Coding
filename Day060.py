def prima(angka):
    if angka <= 1:
        return False
    elif angka == 2:
        return True
    elif angka % 2 == 0:
        return False
    else:
        batas = int(angka**0.5) + 1
        for i in range(3, batas, 2):
            if angka % i == 0:
                return False
        return True

angka_input = int(input("Masukkan angka: "))
if prima(angka_input):
    print(f"{angka_input} adalah bilangan prima.")
else:
    print(f"{angka_input} bukan bilangan prima.")
