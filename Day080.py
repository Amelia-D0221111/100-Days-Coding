def karakter_index_genap(string_input):
    hasil = ""
    for i in range(0, len(string_input), 2):
        hasil += string_input[i]
    return hasil

input_string = input("Masukkan sebuah string: ")

output = karakter_index_genap(input_string)
print("Output:", output)
