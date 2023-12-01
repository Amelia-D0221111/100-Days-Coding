class KeranjangBelanja:
    def __init__(self):
        self.item_list = []

    def tambah_item(self, item):
        self.item_list.append(item)

    def hapus_item(self, item):
        if item in self.item_list:
            self.item_list.remove(item)
        else:
            print(f"{item} tidak ditemukan dalam keranjang belanja.")

    def tampilkan_isi(self):
        if not self.item_list:
            print("Keranjang belanja kosong.")
        else:
            print("Isi keranjang belanja:")
            for item in self.item_list:
                print(item)

# Contoh penggunaan class dengan list
keranjang = KeranjangBelanja()
keranjang.tambah_item('sabun')
keranjang.tambah_item('shampoo')
keranjang.tampilkan_isi()

keranjang.hapus_item('sabun')
keranjang.tampilkan_isi()
