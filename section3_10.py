import pandas as pd

path =  './yemoonsaBigdata-main/datasets/Part5/ex6/'

file = path + '06.01.01-Fire Station Data.csv'
df = pd.read_csv(file, encoding='cp949')

print(df.head())
print(df.tail())
print(df.info())
df1 = df.copy()
df1['신고접수시간'] = pd.to_datetime(df1['신고접수시간'])
df1['출발시간'] = pd.to_datetime(df1['출발시간'])
df1['도착시간'] = pd.to_datetime(df1['도착시간'])
# 신고접수 후 출발시간까지를 대응시간, 출발시간에서 도착시간까지를 출동시간이라 한다. 소방서별 출동시간 평균이 가장 큰
# 보상소의 출동시간 평균을 구하시오. (소수 둘째자리까지)
#1. 대응시간, 출동시간 구하기 --> 초단위로 변경
df1['대응시간'] = (df1['출발시간'] - df1['신고접수시간']).dt.total_seconds()
df1['출동시간'] = (df1['도착시간'] - df1['출발시간']).dt.total_seconds()

print(df1.head())

#2. 소방서별 출동시간 평균 구하기
dg = df1.groupby('소방서ID')['출동시간'].mean()
print(dg.head())
dg = df1.groupby('소방서ID')['출동시간'].mean().sort_values(ascending=False)
dg = dg.reset_index()
print(dg.head())

#3. 가장 큰 소방서의 출동시간 평균을 구하시오. (소수 둘째자리 반올림) loc : location iloc : integer location
result = round(dg['출동시간'][0],2)
result = round(dg.loc[0, '출동시간'], 2)
print(result)