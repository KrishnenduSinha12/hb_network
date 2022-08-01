import numpy as np
import sys
sys.path.append("/home/bappai/Dropbox/Work_Krishnendu/Codes")
from my_functions import *

f=read_xvg("mindist_input.dat",ncol=2)

Pairs=[]
for i in range (len(f[0])):
    Pairs.append((int(f[0][i]),int(f[1][i])))


for j in range (len(Pairs)):
    print("gmx make_ndx -f ../WT_run2.pdb -o new_index.ndx << EOF \n r "+ " " + str(Pairs[j][0]) + "\n r " + " "+str(Pairs[j][1]) + "\n name 10 group1 \n name 11 group2 \n q \nEOF")
    print("wait")
    print ("echo 10 11 |gmx mindist -f ../WT_run2_fit.xtc -s ../WT_run2.tpr -n new_index.ndx -b 0 -e 1000000 -dt 1000 -od mindist_"+str(Pairs[j][0])+"_"+str(Pairs[j][1])+".xvg ")
    print("wait")
    print("rm -rf new_index.ndx")
    print("wait")
    print("\n")





