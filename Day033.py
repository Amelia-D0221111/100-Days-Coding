nama = input("masukkan nama : ")
umur = input("masukkan umur : ")

if nama.isdigit():
    print("nama tidak valid karena berupa angka ")
elif nama.isalpha():
    print(f"nama saya {nama}")
else :
    print("nama kosong")
if umur.isdigit():
    print(f"umur saya {umur}")
elif umur.isalpha():
    print("umur tidak valid karena berupa huruf")
else :
    print("umur kosong")