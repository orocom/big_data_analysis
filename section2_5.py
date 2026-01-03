path = './yemoonsaBigdata-main/datasets/Part5/ex7/'

import pandas as pd

file = path + '07.01.02-fish_weight_data.csv'

print(file)

df = pd.read_csv(file)

print(df.head())
print(df.info())
print(df.describe())

##id 제거

df1 = df.copy()
df1 = df1.drop('id', axis=1)

print(df1.info())

#상관계수 구하기

corr_matrix = df1.corr()
print(corr_matrix)

corr_weight = corr_matrix['Weight'].drop('Weight')
print(corr_weight)
print(corr_weight.max())
print(corr_weight.idxmax())