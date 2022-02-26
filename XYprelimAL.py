import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_AllostaticLoad.csv')

# Dropping participants who are missing any of the information necessary to calculate our preliminary
# score of allostatic load (might be replaced later by switching nan values for mean or
# predicting nan values using other variables, if we want to have a larger sample size)
df = df.dropna(axis=0, how='any')
df = df.loc[df['Sex_T0'] == 1]
df = df.reset_index(drop=True)
stats = df.describe()

# Using 25th or 75th percentile value to determine cutoff, based on whether high or low values are
# typically associated with dysfunction or disease risk`
albuminCutoff = stats['Albumin_T0']['25%']
creatinineCutoff = stats['Creatinine_T0']['75%']
crpCutoff = stats['CReactiveProtein_T0']['75%']
hba1cCutoff = stats['GlycatedHaemoglobin_T0']['75%']
# Not sure about logic of HDL being included
hdlCutoff = stats['HDLCholesterol_T0']['25%']
ldlCutoff = stats['LDLDirect_T0']['75%']
triglycerideCutoff = stats['Triglyceride_T0']['75%']
igfCutoff = stats['IGF1_T0']['25%']
bmiCutoff = stats['BMI_T0']['75%']
dbpCutoff = stats['DiastolicBloodPressure1_T0']['75%']
sbpCutoff = stats['SystolicBloodPressure1_T0']['75%']

# Creating dataframe with only the variables being used to calculate allostatic load
dfPrelim = df[['ID', 'Albumin_T0', 'Creatinine_T0', 'CReactiveProtein_T0', 'GlycatedHaemoglobin_T0',
               'IGF1_T0', 'LDLDirect_T0', 'Triglyceride_T0', 'BMI_T0', 'DiastolicBloodPressure1_T0',
               'SystolicBloodPressure1_T0']]
# Calculating allostatic load index for each participant based on whether their value for
# a given measure is above/below the cutoff determine above
arr = np.full((df.shape[0], 2), -1)
for row in dfPrelim.itertuples():
    index = row[0]
    alloLoad = 0
    arr[index, 0] = row[1]
    # Adds 1 to AL if Albumin level is below or equal to cutoff
    if row[2] <= albuminCutoff:
        alloLoad += 1
    # Adds 1 to AL if Creatinine level is above or equal to cutoff
    if row[3] >= creatinineCutoff:
        alloLoad += 1
    # Adds 1 to AL if CRP level is above or equal to cutoff
    if row[4] >= crpCutoff:
        alloLoad += 1
    # Adds 1 to AL if HbA1c is above or equal to cutoff
    if row[5] >= hba1cCutoff:
        alloLoad += 1
    # Adds 1 to AL if IGF1 level is below or equal to cutoff
    if row[6] <= triglycerideCutoff:
        alloLoad += 1
    # Adds 1 to AL if LDL level is above or equal to cutoff
    if row[7] >= ldlCutoff:
        alloLoad += 1
    # Adds 1 to AL if Triglyceride levels are above or equal to cutoff
    if row[8] >= triglycerideCutoff:
        alloLoad += 1
    # Adds 1 to AL if BMI is above or equal to cutoff
    if row[9] >= bmiCutoff:
        alloLoad += 1
    # Adds 1 to AL if Diastolic blood pressure is above or equal to cutoff
    if row[10] >= dbpCutoff:
        alloLoad += 1
    # Adds 1 to AL if Systolic blood pressure is above or equal to cutoff
    if row[11] >= sbpCutoff:
        alloLoad += 1
    # Assigns total AL to corresponding spot in array
    arr[index, 1] = alloLoad

# Converts array into dataframe
alloLoadCalc = pd.DataFrame(arr, columns=['ID', 'Allostatic_Load_Index'])

# Merges allostatic load calculation with original dataframe using IDs
df = pd.merge(df, alloLoadCalc, on='ID')

# Saves allostatic load index and information used to make it to csv
df.to_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_XY_Calculation.csv', index=False)
plot = plt.hist(df['Allostatic_Load_Index'])