from math import pi as phi  # mengambil nilai phi dari library bawaan python; math


class BangunRuang:
    def luas(self):
        pass

    def volume(self):
        pass


class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        volume = self.sisi**3
        return volume

    def luas(self):
        luas = 6 * (self.sisi**2)
        return luas


class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return volume

    def luas(self):
        luas = 2 * (
            (self.panjang * self.lebar)
            + (self.lebar * self.tinggi)
            + (self.panjang * self.tinggi)
        )
        return luas


class Bola(BangunRuang):
    def __init__(self, jari):
        self.jari = jari

    def volume(self):
        volume = 4 / 3 * phi * (self.jari**3)
        return round(volume, 2)

    def luas(self):
        luas = 4 * phi * (self.jari**2)
        return round(luas, 2)


pilih = ""
while pilih != "4":
    print()
    print(
        """1. Kubus
2. Balok 
3. Bola
4. Berhenti"""
    )
    pilih = input("Masukkan Pilihan: ")

    if pilih == "1":
        sisi = float(input("Sisi: "))

        kubus = Kubus(sisi)
        pilih1 = input("Hitung Luas / Volume? => ").lower()

        if pilih1 == "luas":
            print("Luas kubus: ", kubus.luas())
        elif pilih1 == "volume":
            print("Volume kubus: ", kubus.volume())
        else:
            print("Masukkan inputan yang benar!")

    elif pilih == "2":
        panjang = float(input("Panjang: "))
        lebar = float(input("Lebar: "))
        tinggi = float(input("Tinggi: "))

        balok = Balok(panjang, lebar, tinggi)
        pilih2 = input("Hitung Luas / Volume? => ").lower()

        if pilih2 == "luas":
            print("Luas balok: ", balok.luas())
        elif pilih2 == "volume":
            print("Volume balok: ", balok.volume())
        else:
            print("Masukkan inputan yang benar!")

    elif pilih == "3":
        jari = float(input("Jari-jari: "))

        bola = Bola(jari)
        pilih3 = input("Hitung Luas / Volume? => ").lower()

        if pilih3 == "luas":
            print("Luas bola: ", bola.luas())
        elif pilih3 == "volume":
            print("Volume bola: ", bola.volume())
        else:
            print("Masukkan inputan yang benar!")

    else:
        if pilih != "4":
            print("Masukkan pilihan yang benar!")
