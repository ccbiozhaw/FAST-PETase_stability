from __future__ import print_function
import matplotlib.pyplot as plt
import itertools
import mdtraj as md
import mdtraj.testing
import pandas as pd
import numpy as np
trajs=['EQ_NVT.h5','EQ_NPT.h5','EQ_NPT_free.h5',"production_0.h5"]#,"production_1.h5","production_2.h5","production_3.h5","production_4.h5"]

df=pd.read_excel('hbonds_fast_50.xls')
print(df)
np_df=df.to_numpy()
df_features=[]
for i in np_df:
    hbond=[]
    hbond.append(i[0])
    for traj in trajs:
        for chunk in md.iterload(traj,chunk=5000):#"free_NPT_EQ.pdb")#"NPT_EQ.pdb")#'NVT_EQ.pdb')
            distance = md.compute_distances(chunk, [[int(i[1]),int(i[2])]], periodic=False)
            hbond.extend(distance[::100])
    df_features.append(hbond)
df = pd.DataFrame(df_features)
df.to_csv('hbond_distances.csv',sep=';')

