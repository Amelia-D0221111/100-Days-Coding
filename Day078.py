def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def permutasi(n, r):
    if n < r:
        return "n harus lebih besar atau sama dengan r"
    else:
        hasil_permutasi = faktorial(n) / faktorial(n - r)
        return int(hasil_permutasi)

n = 5
r = 3
hasil = permutasi(n, r)

print(f"Permutasi dari {n} dan {r} adalah: {hasil}")
