import pandas as pd
import statsmodels.api as sm

path = './yemoonsaBigdata-main/datasets/Part5/ex7/'
#file 읽어오기
file = path + '07.03.01-gender_prediction_dataset.csv'
df = pd.read_csv(file)

# print(df.isnull().sum())

df1 = df.copy()

#카테고리 변수를 이진 변수로 변환
df1["Gender"] = df1['Gender'].map({"Male":0, 'Female':1})

# print(df1['Gender'])

#변수 설정
X = df1[['Height', 'Weight', 'ShoeSize']]
y = df1['Gender']

#훈련, 평가 테이블 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify =y, random_state = 123)
# print(X_train, X_test, y_train, y_test)

#모델 생성
#y = ax + b(b-절편, a-기울기)
print(X_train)
X_train = sm.add_constant(X_train)
print(X_train)

lm = sm.Logit(y_train, X_train).fit()

print(lm.summary())

#문1) Weight의 오즈비 (성공 확률과 실패할 확률의 비) x 1, y 1.5 영향을 준다는 의미
import numpy as np
odds_ratios = np.exp(lm.params['Weight']) # coef = log(odds ratio), odds ratio = exp (coef)
print(odds_ratios)

#문2) 모델의 로짓우도(log-likelihood)를 구하시오.

log_likelihood = lm.llf
print(log_likelihood)
#문3) 위 (2)에서 만든 모델로 평가용 데이터를 예측한 결과와 실제값의 오차율을 구하시오. (소수 네자리에서 반올림)
X_test = sm.add_constant(X_test)
y_pred = (lm.predict(X_test) >= 0.5).astype(int)

print(y_pred)
print(y_test)

error_rate = round(np.mean(np.abs(y_pred.values-y_test)), 4)
print(error_rate)

