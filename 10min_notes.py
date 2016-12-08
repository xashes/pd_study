import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20161101', periods=4)
df = pd.DataFrame(np.random.randn(4, 6), index=dates, columns=list('ABCDEF'))
df2 = pd.DataFrame({'A' : 1,
                    'B' : pd.Series(dates, index=[6, 7, 8, 9]),
                    'C' : pd.Series(1, index=[6,7,8,9], dtype='float32'),
                    'D' : np.random.randn(4)})

# setting a new column automatically aligns the data by the indexes
s1 = pd.Series(np.random.randn(6), index=pd.date_range('20161103', periods=6))
print(60*'-')
df.F = s1
df.iat[0, 0] = 0
df.at[dates[0], 'B'] = 0
df.loc[:, 'D'] = np.array([5] * len(df))

# A 'where' operation with setting
df2 = df.copy()
df2[df2 < 0] = -df2

# Missing Data
# Reindexing
df1 = df.reindex(index=dates[0:3], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
# To drop any rows that have missing data.
df3 = df.dropna(how='any')
# Filling missing data
print(df1.fillna(value=99))
# To get the boolean mask where values are nan
print(pd.isnull(df1))

# Operations
# ------------------------------------------------------------
# Stats
# Operations in general exclude missing data
print(df.mean())
print(df.mean(axis=1))

# Apply functions to the data
print(df)
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming
s = pd.Series(np.random.randint(0, 2, size=100))
print(s.value_counts())
