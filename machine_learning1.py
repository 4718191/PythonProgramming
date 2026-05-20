# 머신러닝 분류 654p

# 1. 데이터 수집하기
from sklearn import datasets
iris = datasets.load_iris()

print('iris 키:', iris.keys())
print('특성 이름:', iris['feature_names'])

print('타깃:\n', iris['target'][:150])
print('타깃 이름:', iris['target_names'])

print('데이터 크기:', iris['data'].shape)
print('타깃 크기:', iris['target'].shape)

# 결측지 체크
# 이상치 체크 : 상자 그림

# 2. 데이터 전처리하기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# 3. 모델 생성하기
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3) # 이웃 개수 = 3
knn.fit(X_train, y_train)

# 4. 모델을 이용해 예측하기
import numpy as np

X_new = np.array([[6, 3.5, 5, 1.5]]) # 새로운 데이터

pred = knn.predict(X_new)
print(pred)
print(iris['target_names'][pred])

y_pred = knn.predict(X_test)
print('테스트 세트 예측 값:\n', y_pred)
print('테스트 세트 실제 타깃:\n', y_test)

# 5. 모델 평가하기
print(f'훈련 세트 정확도: {knn.score(X_train, y_train):.3f}')
print(f'테스트 세트 정확도: {knn.score(X_test, y_test):.3f}')