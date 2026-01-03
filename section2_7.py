path = './yemoonsaBigdata-main/datasets/Part5/ex7/'

import pandas as pd

train_file = '07.02.01-sales_train_dataset.csv'
X_test_file = '07.02.02-sales_test_dataset_x.csv'

train = pd.read_csv(path+train_file)
X_test = pd.read_csv(path+X_test_file)

print(train.head())
print(X_test.head())
print(train.describe())
print(X_test.describe())
print(train.info())
print(X_test.info())

# 데이터 전처리
print(train.isnull().sum())
# 변수 구분
col_del = ['BranchName']
col_num = ['Population', 'IncomeGeneratingPopRatio', "AverageIncome"]
col_cat = ['City', "IndustryType"]
col_y = ['Sales']

#3. 머신러닝 모델링
#3.1 데이터 분할
X_train = train[col_cat + col_num]
y_train = train[col_y]
# print(X_train, y_train)

from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train.values.ravel(), test_size=0.3) # 같은 메모리 공유
# X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train.values.flatten(), test_size=0.3) # Copy
print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

#3.2 수치형 데이터 스케일링 작업
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_tr[col_num])

X_tr[col_num] = scaler.transform(X_tr[col_num])
X_val[col_num] = scaler.transform(X_val[col_num])
X_test[col_num] = scaler.transform(X_test[col_num])

# print(X_tr[col_num])

#3.3 범주형 변수 인코딩 (라벨, 원핫 인코딩)
from sklearn.preprocessing import LabelEncoder

X = pd.concat([X_tr[col_cat], X_test[col_cat]])

print(X)

for col in col_cat:
    le = LabelEncoder()
    le.fit(X[col])

    X_tr[col] = le.transform(X_tr[col])
    X_val[col] = le.transform(X_val[col])
    X_test[col] = le.transform(X_test[col])
    print(col, le.classes_)
    print(X_tr[col])

#3.4 모형학습
from sklearn.ensemble import RandomForestRegressor
model_rf = RandomForestRegressor()
model_rf.fit(X_tr, y_tr)

from xgboost import XGBRegressor
model_xgb = XGBRegressor(random_state=123)
model_xgb.fit(X_tr, y_tr)

#3.5 검증데이터 검증 예측값 생성
pred_rf = model_rf.predict(X_val)
pred_xg = model_xgb.predict(X_val)
print(pred_rf, pred_xg)

#4. 머신러닝 모델 평가
from sklearn.metrics import mean_squared_error

rmse_rf = mean_squared_error(y_val, pred_rf, squared=False)
rmse_xg = mean_squared_error(y_val, pred_xg, squared=False)

print(f"rmse_rf : {rmse_rf}, rmse_xg : {rmse_xg}")

#4.1 하이퍼파라미터 튜닝(생략)

#답안 제출
pred = model_rf.predict(X_test[col_cat + col_num])
pd.DataFrame({'BranchName': X_test['BranchName'], 'Sales' : pred}).to_csv('0030000000.csv', index=False)

import pandas as pd
df_y = pd.read_csv('./yemoonsaBigdata-main/datasets/Part5/ex7/07.02.03-sales_test_dataset_y.csv')
df_pred = pd.read_csv('0030000000.csv')
print(df_y)
from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(df_y['Sales'], df_pred['Sales'], squared=False)
print(f"rmse : {rmse}")
