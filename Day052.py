def hitung_faktorial(bilangan):
    if bilangan < 0:
        return "Faktorial hanya didefinisikan untuk bilangan non-negatif."
    elif bilangan == 0 or bilangan == 1:
        return 1
    else:
        faktorial = 1
        for i in range(2, bilangan + 1):
            faktorial *= i
        return faktorial

bilangan_input = int(input("Masukkan bilangan untuk menghitung faktorial: "))
hasil_faktorial = hitung_faktorial(bilangan_input)

print(f"Faktorial dari {bilangan_input} adalah: {hasil_faktorial}")
