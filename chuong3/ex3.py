import numpy as np

arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
arr_c = np.intersect1d(arr_a, arr_b)
arr_d = np.setdiff1d(arr_a, arr_b)
arr_e = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("Mảng arr_c:", arr_c)
print("Mảng arr_d:", arr_d)
print("Mảng arr_f:", arr_f)