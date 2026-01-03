

path = './yemoonsaBigdata-main/datasets/Part5/ex7/'

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import scipy.stats as stats

file = path + '07.01.01-students_scores.csv'

df = pd.read_csv(file)

print(df.head())
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())

# df1 = df.fillna(0)
# df1 = df.fillna('missing')
# df1 = df.fillna(method='bfill')
# df1 = df.fillna(method='ffill')
# df1 = df.fillna(method='pad')
# df1 = df.fillna(df.mean())
# df1 = df.fillna(df.mean()['Statistics'])
df1 = df.interpolate(method='linear')
# df1 = df.interpolate(method='polynomial', order=2)
print(df1.head())
df1 = df1.fillna(method='bfill')
print(df1.head())


print(df.info())
df2 = df.drop(labels='student id', axis=1)
print(df2.head())
print(df2.count())
print(df2.count().idxmax())
drop_df = df2[df2.count().idxmax()].dropna()
print(drop_df.info())
print(drop_df.shape)
print(drop_df)

#1. scipy.stats
mps_score = round(stats.zscore(drop_df).max(),2)
print(f"scipy mps_score: {mps_score}")
#2. sklearn
scaler = StandardScaler()
scaler.fit(drop_df.values.reshape(-1,1)) #2차원으로 바꿔주고 실행
scaled_df = scaler.transform(drop_df.values.reshape(-1,1)) # train data에서는 fit_transform도 가능 test data는 transform만 씀
mps_score = round(scaled_df.max(), 2)
print(f"sklearn: {mps_score}")