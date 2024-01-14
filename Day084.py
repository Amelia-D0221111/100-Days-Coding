def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Elemen {target} ditemukan di indeks {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return f"Elemen {target} tidak ditemukan dalam array"

data_biner = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_biner = 5
hasil_biner = binary_search(data_biner, target_biner)
print(hasil_biner)
