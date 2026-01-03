
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', '{:.10f}'.format)

# print(dir(pd))

# print(help(pd.to_datetime))

import sklearn
from sklearn import preprocessing

# print(sklearn.__all__)
# print(dir(preprocessing))
# print(help(preprocessing.LabelEncoder))

# from scipy import stats
# print(dir(stats))
# print(help(stats.ttest_rel))

# import statsmodels.api as sm
# print(dir(sm))
# print(dir(sm.formula))
# print(help(sm.formula.ols))

import statsmodels.api as sm
import statsmodels

print(dir(statsmodels))
print("statsmodels.stats:")
print(dir(statsmodels.stats))
print("statsmodels.stats.anova:")
print(dir(statsmodels.stats.anova))
print("statsmodels.stats.anova.anova_lm:")
print(help(statsmodels.stats.anova.anova_lm))