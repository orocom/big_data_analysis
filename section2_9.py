import pandas as pd
import statsmodels.api as sm

path = './yemoonsaBigdata-main/datasets/Part5/ex7/'
#file 읽어오기
file = path + '07.03.02-used_car_price_dataset.csv'
df = pd.read_csv(file)
# print(df.head())
# print(df.info())
# print(df.describe())

#모델생성
#1. 데이터 전처리
print(df.info()) #transmission, fuelType
print(df['transmission'].unique())
print(df['fuelType'].unique())
df1 = df.copy()

#카테고리 Value
df1['transmission'] = df1['transmission'].map({'Manual':0, 'Automatic':1, 'Semi-Auto':2})
df1['fuelType'] = df1['fuelType'].map({'Petrol':0, 'Diesel':1, 'Hybrid':2})

#독립 변수, 종속 변수설정
X_cols = ['year', 'transmission', 'mileage', 'fuelType', 'mpg', 'engineSize']
y_cols = ['price']
#독립변수, 종속변수 데이터 분리
X = df1[X_cols]
y = df1[y_cols]

#모델 생성
X = sm.add_constant(X)
# print(X)
model = sm.OLS(y, X).fit()
print(model.summary())
#문제 풀기
#1) 다중회귀분석 모형의 결정계수를 구하시오
r_squared = model.rsquared
# print(r_squared)
#2) 독립변수 중 회귀계수가 가장 큰 변수와 값을 구하여 튜플 타입으로 출력하시오.
coefs = model.params
print(coefs)
max_coef = coefs.idxmax(), coefs.max()
print(max_coef)

#3) 독립변수 중 p-value가 가장 낮은 변수와 값을 구하여 튜플 타입으로 출력하시오.
pvalues = model.pvalues
min_pvalue = pvalues.idxmin(), pvalues.min()
print(min_pvalue)