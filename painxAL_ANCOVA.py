import pandas as pd
import numpy as np
import pingouin as pg

pain = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/Pain_T0.csv')
pain = pain.rename(columns={'eid':'ID'})
pain = pain.drop(columns={'Age_T0', 'Sex_T0'})
XX_AL = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_XX_Calculation.csv')
XY_AL = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_XY_Calculation.csv')
AL = XX_AL.append(XY_AL)
df = pd.merge(AL, pain, on='ID')

arr = np.arr = np.full((df.shape[0], 2), -1)
for row in df.itertuples():
    index = row[0]
    arr[index, 0] = row[1]
    if row[33] == 0:
        arr[index, 1] = 0
    elif row[33] == 1:
        arr[index, 1] = 1
    elif row[33] > 1:
        arr[index, 1] = 2

status = pd.DataFrame(arr, columns=['ID', 'painStatus'])
df = pd.merge(df, status, on='ID')
anc = pg.ancova(data=df, dv='Allostatic_Load_Index', covar=['Age_T0','Sex_T0'], between='painStatus')