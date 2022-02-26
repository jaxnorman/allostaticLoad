import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_Calculation.csv')
df = df.drop(columns=['Unnamed: 0'])
df.columns
XX = df.loc[df['Sex_T0'] == 0]
XY = df.loc[df['Sex_T0'] == 1]

sns.set_theme(style='ticks')
XX_ALxAge = sns.regplot(x='Age_T0', y='Allostatic_Load_Index', data=XX)
XY_ALxAge = sns.regplot(x='Age_T0', y='Allostatic_Load_Index', data=XY)
