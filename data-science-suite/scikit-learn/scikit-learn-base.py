from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加載數據集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 拆分數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# 數據標準化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 建立 k-近鄰分類器
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(X_train_std, y_train)

# 進行預測
y_pred = knn.predict(X_test_std)

# 計算準確率
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# 更多功能
# Scikit-learn 提供了許多用於機器學習的工具和演算法，包括：

# 各種監督學習和無監督學習的演算法。
# 各種特徵提取和數據預處理的方法。
# 各種模型選擇和評估的工具。