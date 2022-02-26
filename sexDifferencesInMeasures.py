import pandas as pd
df = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_Calculation.csv')
df = df.drop(columns=['Unnamed: 0'])
XX = df.loc[df['Sex_T0'] == 0]
XY = df.loc[df['Sex_T0'] == 1]
XXstat = XX.describe()
XYstat = XY.describe()