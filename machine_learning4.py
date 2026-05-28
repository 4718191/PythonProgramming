from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# 데이터 수집하기
diabetes = datasets.load_diabetes()
print('diabetes 키:', diabetes.keys())
print('데이터:\n', diabetes['data'][:3])
print('특성 이름:', diabetes['feature_names'])
print('타깃:\n', diabetes['target'])
print('데이터 크기:', diabetes['data'].shape)
print('타깃 크기:', diabetes['target'].shape)

# 데이터 전처리하기
X_train, X_test, y_train, y_test = train_test_split(diabetes['data'], diabetes['target'], random_state=0)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# 모델 생성
lr = LinearRegression()
lr.fit(X_train, y_train)

print('절편:', np.round(lr.intercept_,3))
print('계수:', np.round(lr.coef_,3))

# 모델 이용해 예측하기
pred = lr.predict(X_test)
print('테스트 세트 예측 값 :\n', np.round(pred[:10],3))
print('테스트 세트 실제 타깃 :\n', y_test[:10])

# 모델 평가
print(f'훈련 세트 점수: {lr.score(X_train, y_train):.3f}')
print(f'테스트 세트 점수: {lr.score(X_test, y_test):.3f}')
