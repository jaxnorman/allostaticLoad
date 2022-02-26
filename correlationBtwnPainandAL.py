import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
# import confounds as cn
pain = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/expPain_chronicPain.csv')
pain = pain.drop(columns={'Unnamed: 0'})
pain = pain.rename(columns={'eid': 'ID'})
alloLoad = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_Calculation.csv')
alloLoad = alloLoad.drop(columns={'Unnamed: 0'})
df = pd.merge(pain, alloLoad, on='ID')
stat = df.describe()
df = df.loc[df['Sex_T0'] == 1]
correlation = df.corr()
pr = stats.pearsonr(df['Allostatic_Load_Index'], df['Age_T0'])
sr = stats.spearmanr(df['Allostatic_Load_Index'], df['Age_T0'])

plot = plt.hist(df['Allostatic_Load_Index'])