arr = []
def jumlah(x):
    while True:
        angka = int(input("angka -> "))
        arr.append(angka)
        print(arr)
        total = sum(arr)
        print(total)

        if total >= x:
            break

jumlah(10)
