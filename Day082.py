def hitung_kemunculan_kata(string_input):
    kata = string_input.split()
    frekuensi = {}

    for k in kata:
        if k in frekuensi:
            frekuensi[k] += 1
        else:
            frekuensi[k] = 1

    return frekuensi

input_string = input("Masukkan sebuah string: ")

hasil = hitung_kemunculan_kata(input_string)
print("Frekuensi kemunculan kata:", hasil)
