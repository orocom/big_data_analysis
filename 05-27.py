import pandas as pd
pd.set_option('display.max_columns', None) #컬럼(열)
pd.set_option('display.max_rows', None) # 행
pd.set_option('display.float_format', '{:,.10f}'.format) # 소수 10자리까지 출력

print("#1")
print(dir(pd))

print("#2")
help(pd.to_datetime)





