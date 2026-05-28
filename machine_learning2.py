from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 데이터 수집하기
wine = datasets.load_wine()
print('wine 키:', wine.keys())
print('데이터:\n', wine['data'][:5])
print('특성 이름:', wine['feature_names'])
print('타깃:\n', wine['target'][:5])
print('타깃 이름:', wine['target_names'])
print('데이터 크기:', wine['data'].shape)
print('타깃 크기:', wine['target'].shape)

# 데이터 전처리하기
X_train, X_test, y_train, y_test = train_test_split(wine['data'], wine['target'], random_state=0)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# 모델 생성하기
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 모델 이용해 예측하기
y_pred = knn.predict(X_test)
print('테스트 세트 예측 값:\n', y_pred)
print('테스트 세트 실제 타깃:\n', y_test)

# 모델 평가하기
print(f'훈련 세트 정확도: {knn.score(X_train, y_train):.3f}')
print(f'테스트 세트 정확도: {knn.score(X_test, y_test):.3f}')
