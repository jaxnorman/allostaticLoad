import pandas as pd
import numpy as np

df = pd.read_csv('~/Desktop/UKBB_Data/UKB_NoBrain_500K_V3.csv')
# col = df.columns
# col_names = col.to_series()
# col_names.to_csv('~/Desktop/noBrain_500K_V3_columns.csv')
df.columns
aLoad = df[['eid', 'Sex_T0', 'YearBirth_T0', 'DateAssessment_T0', 'DateAssessment_T2',
           '21001-0.0', '21000-2.0', 'DiastolicBloodPressure1_T0',
           'DiastolicBloodPressure2_T0', 'SystolicBloodPressure1_T0',
           'SystolicBloodPressure2_T0', 'DiastolicBloodPressure1_T2',
           'DiastolicBloodPressure2_T2', 'SystolicBloodPressure1_T2',
           'SystolicBloodPressure2_T2', '6145-0.0', '6145-0.1', '6145-0.2', '6145-0.3',
           '6145-0.4', '6145-0.5', '6145-2.0', '6145-2.1', '6145-2.2', '6145-2.3', '6145-2.4', '6145-2.5']]
aLoad.rename(columns={'21001-0.0':'BMI_T0', '21000-2.0':'BMI_T2', 'DiastolicBloodPressure1_T0':'DiastolicBP1_T0',
                      'DiastolicBloodPressure2_T0':'DiastolicBP2_T0', 'SystolicBloodPressure1_T0':'SystolicBP1_T0',
                      'SystolicBloodPressure2_T0':'SystolicBP2_T0', 'DiastolicBloodPressure1_T2':'DiastolicBP1_T2',
                      'DiastolicBloodPressure2_T2':'DiastolicBP2_T2', 'SystolicBloodPressure1_T2':'SystolicBP1_T2',
                      'SystolicBloodPressure2_T2':'SystolicBP2_T2', '6145-0.0':'stressEvent1_T0',
                      '6145-0.1':'stressEvent2_T0', '6145-0.2':'stressEvent3_T0', '6145-0.3':'stressEvent4_T0',
                      '6145-0.4':'stressEvent5_T0', '6145-0.5':'stressEvent6_T0', '6145-2.0':'stressEvent1_T2',
                      '6145-2.1':'stressEvent2_T2', '6145-2.2':'stressEvent3_T2', '6145-2.3':'stressEvent4_T2',
                      '6145-2.4':'stressEvent5_T2', '6145-2.5':'stressEvent6_T2'})
