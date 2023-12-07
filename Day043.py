class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, nilai):
        self.nilai.append(nilai)

    def rata_rata_nilai(self):
        if len(self.nilai) == 0:
            return 0
        else:
            return sum(self.nilai) / len(self.nilai)


mahasiswa1 = Mahasiswa("Amelia" , "D0221111")


mahasiswa1.tambah_nilai(90)


print(f"Rata-rata nilai {mahasiswa1.nama}: {mahasiswa1.rata_rata_nilai()}")
