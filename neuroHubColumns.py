import pandas as pd

df = pd.read_csv('~/Desktop/neurohubColumns.csv')

alloLoad = df[['eid', '31-0.0', '21003-0.0', '21003-2.0', ''
                                                          ']]
alloLoad.rename(columns={'31-0.0':'Sex_T0', '21003-0.0':'Age_T0', '21003-2.0':'Age_T2',
                         })