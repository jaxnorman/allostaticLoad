import pandas as pd
import seaborn as sns
import pingouin as pg
XX_AL = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_XX_Calculation.csv')
XY_AL = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/UKBB_Preliminary_Allostatic_Load_XY_Calculation.csv')
pain_T0 = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/Pain_T0.csv')
pain_T0 = pain_T0.rename(columns={'eid':'ID'})
pain_T0 = pain_T0.drop(columns={'Age_T0', 'Sex_T0'})
XX_pain_AL = pd.merge(XX_AL, pain_T0, on='ID')
XX_pain_AL.columns
XX_partialCorr_num = pg.partial_corr(data=XX_pain_AL, x='Allostatic_Load_Index', y='NumberChronicPainTypes_T0', covar='Age_T0')
XY_pain_AL = pd.merge(XY_AL, pain_T0, on='ID')
XY_partialCorr_num = pg.partial_corr(data=XY_pain_AL, x='Allostatic_Load_Index', y='NumberChronicPainTypes_T0', covar='Age_T0')
XX_partialCorr_widespread = pg.partial_corr(data=XX_pain_AL, x='Allostatic_Load_Index', y='WidespreadPainLastMonth_T0', covar='Age_T0')
XY_partialCorr_widespread = pg.partial_corr(data=XY_pain_AL, x='Allostatic_Load_Index', y='WidespreadPainLastMonth_T0', covar='Age_T0')
XX_partialCorr_chronic = pg.partial_corr(data=XX_pain_AL, x='Allostatic_Load_Index', y='ChronicPain_T0', covar='Age_T0')
XX_partialCorr_acute = pg.partial_corr(data=XX_pain_AL, x='Allostatic_Load_Index', y='AcutePain_T0', covar='Age_T0')
XY_partialCorr_chronic = pg.partial_corr(data=XY_pain_AL, x='Allostatic_Load_Index', y='ChronicPain_T0', covar='Age_T0')
XY_partialCorr_acute = pg.partial_corr(data=XY_pain_AL, x='Allostatic_Load_Index', y='AcutePain_T0', covar='Age_T0')