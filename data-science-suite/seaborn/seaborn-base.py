import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 創建數據
data = np.random.randn(1000)

# 繪製直方圖和核密度估計圖
sns.distplot(data, kde=True, rug=False)

plt.show()

# sns.boxplot：繪製箱型圖。
# sns.violinplot：繪製小提琴圖。
# sns.pairplot：繪製成對的二維分布圖。
# sns.heatmap：繪製熱圖。