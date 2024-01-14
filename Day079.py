def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def kombinasi(n, r):
    if n < r:
        return "n harus lebih besar atau sama dengan r"
    else:
        hasil_kombinasi = faktorial(n) / (faktorial(r) * faktorial(n - r))
        return int(hasil_kombinasi)

n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

hasil = kombinasi(n, r)
print(f"Kombinasi dari {n} dan {r} adalah: {hasil}")
