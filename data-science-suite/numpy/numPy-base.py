import numpy as np

# 創建一維數組
a = np.array([1, 2, 3])
print(a)

# 創建二維數組
b = np.array([[1, 2], [3, 4]])
print(b)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 數組加法
print(a + b)  # 輸出：[5 7 9]

# 數組乘法
print(a * b)  # 輸出：[4 10 18]

# 數組的元素級別的乘方
print(a ** 2)  # 輸出：[1 4 9]

# # # # # # # # # # # # # # # # # # # # # 

# dot product
print(a.dot(b))  # 輸出：32 這是1*4 + 2*5 + 3*6

# 引入 numpy 模組
np1 = np.array([1, 2, 3])
np2 = np.array([3, 4, 5])

# 陣列相加
print(np1 + np2) # [4 6 8]

# 顯示相關資訊
print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別