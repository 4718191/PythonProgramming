from sklearn import datasets

housing = datasets.fetch_california_housing()
print(housing.keys())

print('데이터:\n', housing['data'][:3])
print('특성 이름:', housing['feature_names'])
print('타깃:\n', housing['target'][:3])
print('타깃 이름:', housing['target_names'])
print('데이터 크기:', housing['data'].shape)
print('타깃 크기:', housing['target'].shape)

# 2. 데이터 전처리하기
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(housing['data'], housing['target'], random_state=0)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# 3. 모델 생성하기
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

import numpy as np

print('절편:', lr.intercept_)
print('계수:', np.round(lr.coef_,3))

# 4. 모델을 이용해서 예측하기
pred = lr.predict(X_test)
print('테스트 세트 예측 값 :\n', np.round(pred[:10],3))
print('테스트 세트 실제 타깃 :\n', y_test[:10])

# 5. 모델 평가
print(f'훈련 세트 점수: {lr.score(X_train, y_train):.3f}')
print(f'테스트 세트 점수: {lr.score(X_test, y_test):.3f}')
