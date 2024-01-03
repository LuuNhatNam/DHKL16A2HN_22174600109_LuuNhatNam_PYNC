import numpy as np
arr = np.arange(10)
arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]
print("Mảng arr_odd (các số lẻ):", arr_odd)
print("Mảng arr_even (các số chẵn):", arr_even)
arr_update_1 = np.where(arr % 2 == 0, arr, 100)
print("Mảng arr_update_1:", arr_update_1)