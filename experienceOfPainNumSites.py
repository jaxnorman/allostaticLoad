import pandas as pd
import numpy as np
df = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/expPain_chronicPain.csv')
df = df.drop(columns={'Unnamed: 0'})
arr = np.full((df.shape[0], 3), -1)
for row in df.itertuples():
    index = row[0]
    arr[index, 0] = row[1]
    numSites = 0
    if row[2] == 0:
        arr[index, 1] = 0
        arr[index, 2] = 0
    elif row[3] == 1:
        arr[index, 2] = 1
    else:
        for x in range(4, 16):
            if -100 < row[x] < 11.0:
                numSites = numSites + 1
        arr[index, 1] = numSites
        arr[index, 2] = 0

sites = pd.DataFrame(arr, columns=['eid', 'painSites', 'widespreadPain'])
df = pd.merge(df, sites, on='eid')
df.to_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/expPain_numSites.csv', index=False)