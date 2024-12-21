from __future__ import print_function
import matplotlib.pyplot as plt
import itertools
import mdtraj as md
import mdtraj.testing
import pandas as pd
trajs=['EQ_NVT.h5','EQ_NPT.h5','EQ_NPT_free.h5',"production_0.h5","production_1.h5","production_2.h5","production_3.h5","production_4.h5"]
hbond_list=[]
for traj in trajs:
    for chunk in md.iterload(traj,chunk=5000):#"free_NPT_EQ.pdb")#"NPT_EQ.pdb")#'NVT_EQ.pdb')
        hbonds = md.baker_hubbard(chunk, periodic=False)
        label = lambda hbond : '%s -- %s' % (chunk.topology.atom(hbond[0]), chunk.topology.atom(hbond[2]))
        resid_list = ["121","172","186","192","193","204","224","233","234"]
        for index, hbond in enumerate(hbonds):
                string=str(label(hbond))
                for id in resid_list:
                    if id in string:
                        hbond_list.append([string,hbond[0],hbond[2]])
                        print(hbond_list)

df = pd.DataFrame(hbond_list)
writer = pd.ExcelWriter('h_bonds.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='h_bonds', index=False)
writer.save()


