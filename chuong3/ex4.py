import numpy as np

array_zeros = np.zeros(10)
array_zeros[4] = 1
array_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = array_k[array_k != 0]
arr_h = np.arange(10, 25)
arr_h_reverse = np.flip(arr_h)
print("Mảng array_zero:", array_zeros)
print("Mảng arr_h:", arr_h)
print("Danh sách theo thứ tự đảo ngược của arr_h:", arr_h_reverse)
print("Mảng arr_1:", arr_1)
arr_1 = np.append(arr_1, [10, 20])
print("Mảng arr_1 sau khi thêm 10 và 20:", arr_1)
arr_1 = np.insert(arr_1, 5, 100)
print("Mảng arr_1 sau khi thêm 100 vào index=5:", arr_1)
arr_1 = np.delete(arr_1, 5)
print("Mảng arr_1 sau khi xóa phần tử tại index=5:", arr_1)