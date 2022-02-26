import pandas as pd

df = pd.read_csv('~/Desktop/UKBB_Data/CC_Files/UKB_NoBrain_500K_V3.csv')
pain = df[['eid', 'Sex_T0', 'Age_T0', 'Present_at_T0', 'PainLastMonth_T0', 'SingleSitePainLastMonth_T0',
           'MultisitePainLastMonth_T0', 'WidespreadPainLastMonth_T0', 'NumberPainTypesLastMonth_T0',
           'AcutePain_T0', 'NumberAcutePainTypes_T0', 'ChronicPain_T0', 'ChronicHeadaches_T0',
           'ChronicFacialPain_T0', 'ChronicNeckShoulderPain_T0', 'ChronicBackPain_T0',
           'ChronicStomachAbdominalPain_T0','ChronicHipPain_T0', 'ChronicKneePain_T0',
           'NumberChronicPainTypes_T0']]
pain.to_csv('~/Desktop/UKBB_Data/CC_Files/Derived_Files/Pain_T0.csv', index=False)