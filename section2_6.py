path = './yemoonsaBigdata-main/datasets/Part5/ex7/'

import pandas as pd

file = path + '07.01.03-apartment_prices_dataset.csv'
df = pd.read_csv(file)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

#각 독립변수의 이상치를 사분위수를 기준으로 측정하고 이상치가 가장 많은 독립변수를 구하시오.
#이때 결측치를 먼저 제거한 후 이상치를 구하시오. (이상치는 (1Q-1.5IQR) 보다 작거나 (3Q+1.5IQR)보다 큰 값이며, IQR은 Q3에서 Q1을 뺀 값임)

#결측치 제거하기
df1 = df.copy()
print(df1.info())
df1 = df1.dropna()

#이상치 구하기
print(df1.columns)
cols = list(df1.columns)
print(cols)

outlier_cnt_per_var = {}

for c in cols:
    q1, q3 = df[c].quantile([0.25, 0.75])
    print((q1,q3))
    iqr = q3 - q1
    cond1 = (df[c] < (q1-1.5*iqr))
    cond2 = (df[c] > (q3+1.5*iqr))
    outlier_cnt = sum(cond1 | cond2)
    print(cond1)
    print(cond2)
    print(outlier_cnt)
    outlier_cnt_per_var[c] = outlier_cnt

print(outlier_cnt_per_var)
print(outlier_cnt_per_var.keys())
print(outlier_cnt_per_var.values())
min_key = min(outlier_cnt_per_var, key=outlier_cnt_per_var.get)
max_key = max(outlier_cnt_per_var, key=outlier_cnt_per_var.get)
print(max_key)
