class Kubus():
    def __init__(self, sisi):
        self.sisi = sisi

    def volume (self):
        v_k = self.sisi**3
        print("volume kubus adalah : " , v_k)

    def luas (self):
        l_k = 6 * self.sisi**2
        print("luas kubus adalah : " , l_k)

class Balok():
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume (self):
        v_b = self.panjang * self.lebar * self.tinggi
        print("volume balok adalah : " , v_b)
        
    def luas (self):
        l_b = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        print("luas balok adalah : " , l_b)

class Bola():
    def __init__(self, jari):
        self.jari = jari

    def volume (self):
        v_b = 4/3 * 22/7 * self.jari**3
        print("volume Bola adalah : " , round(v_b,2))

    def luas (self):
        l_b = 4 * 22/7 * self.jari**2
        print("luas Bola adalah : " , round(l_b,2))

while True:
    print()
    print("""Bangun Ruang yang akan di hitung
1. Balok
2. Kubus
3. Bola
4. Berhenti""")
    pilihan = input("=> ")

    if pilihan == '1':
        p = float(input("Masukkan Panjang: "))
        l = float(input("Masukkan Lebar: "))
        t = float(input("Masukkan Tinggi: "))
        balok = Balok(p, l, t)
        print()
        print('''Ketik 1 atau 2 untuk menghitung salah satunya
1.Menghitung Volume
2. Menghitung Luas''')
        pilihan = input("=>")
        if pilihan == "1":
            balok.volume()
        elif pilihan == "2":
            balok.luas()
        else :
            break
    elif pilihan == '2':
        s = float(input("Masukkan Sisi: "))
        kubus = Kubus(s)
        print()
        print('''Ketik 1 atau 2 untuk menghitung salah satunya
1.Menghitung Volume
2. Menghitung Luas''')
        pilihan = input("=>")
        if pilihan == "1":
            kubus.volume()
        elif pilihan == "2":
            kubus.luas()
        else :
            break
    elif pilihan == '3':
        j = float(input("Masukkan jari: "))
        bola = Bola (j)
        print()
        print('''Ketik 1 atau 2 untuk menghitung salah satunya
1.Menghitung Volume
2. Menghitung Luas''')
        pilihan = input("=>")
        if pilihan == "1":
            bola.volume()
        elif pilihan == "2":
            bola.luas()
        else :
            break
    elif pilihan == '4':
        break
    else :
        print("inputan salah") 


        
