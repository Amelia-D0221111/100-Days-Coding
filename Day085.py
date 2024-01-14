def tampilkan_terbalik(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])

data = [1, 2, 3, 4, 5]
print("Isi list secara terbalik:")
tampilkan_terbalik(data)
