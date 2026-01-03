import pandas as pd

path =  './yemoonsaBigdata-main/datasets/Part5/ex6/'
file = path + '06.01.02-Elementary School Data.csv'
df = pd.read_csv(file)

#풀이
#교사 1인당 학생 수가 가장 많은 학교를 찾은 후 그 학교의 전체 학생 수를 구하시오.
df1 = df.copy()

# print(df1.head())
# print(df1.tail())
# print(df1.describe())
# print(df1.info())
# print(df['School Name'].unique())

#전체 학생수 구하기
df1['Students'] = df1['1G Students'] + df1['2G Students'] + df1['3G Students'] + df1['4G Students'] + df1['5G Students'] + df1['6G Students']
# print(df1['Students'])
# print(df1)

df1['student per Teachers'] = df1['Students'] / df1['Teachers']
print(df1['student per Teachers'])
print(df1.head())

#교사 1인당 학생수가 가장 많은 학교 찾기
df2 = df1.sort_values(by=['student per Teachers'], ascending=False).reset_index()
print(df2)
max_idx = df1['student per Teachers'].idxmax()
print(max_idx)

#전체 학생수 구하기
result = df2.loc[0, 'Students']
result1 = df1.loc[max_idx, 'Students']
print(result)
print(result1)

print(dir(pd))
import sklearn
print(sklearn.__all__)
from sklearn import preprocessing
print(preprocessing.__all__)
print(help(preprocessing.LabelEncoder))

# 결과
# 교사 1인당 학생 수가 가장 많은 학교의 전체 학생 수
# 1. df2.loc[0, 'Students']
# 2. df1.loc[max_idx, 'Students']
# 3. df1['Students'].max()
# 4. df1['Students'].idxmax()
# 5. df1['Students'].max() == df2.loc[0, 'Students']
# 6. df1['Students'].idxmax() == max_idx
# 7. df1['Students'].max() == result1
# 8. df1['Students'].idxmax() == max_idx
# 9. df1['Students'].max() == result
# 10. df1['Students'].idxmax() == max_idx
# 11. df1['Students'].max() == result
# 12. df1['Students'].idxmax() == max_idx
# 13. df1['Students'].max() == result
# 14. df1['Students'].idxmax() == max_idx
# 15. df1['Students'].max() == result
# 16. df1['Students'].idxmax() == max_idx
# 17. df1['Students'].max() == result
# 18. df1['Students'].idxmax() == max_idx
# 19. df1['Students'].max() == result
# 20. df1['Students'].idxmax() == max_idx
# 21. df1['Students'].max() == result
# 22. df1['Students'].idxmax() == max_idx
# 23. df1['Students'].max() == result
# 24. df1['Students'].idxmax() == max_idx
# 25. df1['Students'].max() == result
# 26. df1['Students'].idxmax() == max_idx
# 27. df1['Students'].max() == resultdw
