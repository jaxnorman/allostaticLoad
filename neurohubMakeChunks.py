import sys
import pandas as pd
start = sys.argv[1]
df = pd.read_csv('/project/rpp-aevans-ab/neurohub/ukbb/tabular/current.csv', skiprows=start, nrows=10000)
df.to_csv('home/projects/ctb-vachonpe/xnorman/AllostaticLoad/Chunks/chunk' + start + '.csv')

