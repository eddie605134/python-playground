import matplotlib.pyplot as plt
import numpy as np

# 創建數據
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 創建一個圖形
# plt.figure()

# # 在圖形中添加一個繪圖區域
# plt.subplot()

# # 繪製線條
# plt.plot(x, y)

# # 顯示圖形
# plt.show()

plt.figure()
plt.subplot()

plt.plot(x, y, label='sin(x)')
plt.title('A Simple Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()