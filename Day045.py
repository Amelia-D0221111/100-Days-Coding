def sapa(nama):
    def dapatkan_sapaan():
        return "Halo"
    
    print(f"{dapatkan_sapaan()}, {nama}!")

sapa("Amelia")