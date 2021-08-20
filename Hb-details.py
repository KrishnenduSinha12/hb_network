import numpy as np
import pandas as pd
import argparse

parser=argparse.ArgumentParser(description="H-bonding-network input requirs two files")
parser.add_argument("-f1", help="file1",required=True)
parser.add_argument("-f2", help="file2",required=True)
parser.add_argument("-c",  help="cutoff",required=False,default=10)
args=parser.parse_args()

F1=args.f1
F2=args.f2
crit=float(args.c)

fo1=open(F1,"r")
fo2=open(F2,"r")

p1=fo1.readlines()
p2=fo2.readlines()
lp1=len(p1)
lp2=len(p2)
pp1=[]
pp2=[]
for i in range(2,lp1):
    pp1.append(p1[i].split())
for i in range(2,lp2):
    pp2.append(p2[i].split())
lpp1=len(pp1)
lpp2=len(pp2)

WT={}
SP={}
change={}       #all bonds whose change above critical value = crit
keys=[]         #appending all the keys in a single list
for i in range(lpp1):
    k=pp1[i][0]+'--'+pp1[i][1]
    v=float(pp1[i][2][0:-1])
    WT.update({k:v})
    keys.append(k)

#crit=float(input("Enter the percentage above which change will be considered : "))


for i in range(lpp2):
    k=pp2[i][0]+'--'+pp2[i][1]
    v=float(pp2[i][2][0:-1])
    SP.update({k:v})
    if WT.get(k,0)==0:
        keys.append(k)
lk=len(keys)
# This part not necessary till 44
for i in range(lk):
    j=keys[i]
    l=SP.get(j,0)
    m=WT.get(j,0)
    n=l-m
    if abs(n)>=crit:
        change.update({j:n})

# Printing the results to the destined file
final=[]
for i in range(lk):
    j=keys[i]
    l=WT.get(j,0)
    m=SP.get(j,0)
    n=m-l
    final.append(j+ " " + str(round(l,2))[0:5] + " " +str(round(m,2))[0:5] + " " +str(round(n,2))[0:6])

final2=[]
for i in range(lk):
    #print(final[i].split()[3])
    if abs(float(final[i].split()[3]))>=crit:
        final2.append(final[i].split())
#print(final2)
lf=len(final2)
x=" "
final3=[]
for i in range(lf):
    lc1=len(final2[i][0])
    lc2=len(final2[i][1])
    lc3=len(final2[i][2])
    k1=24-lc1
    k2=5-lc2
    k3=5-lc3
    final3.append(final2[i][0]+(6+k1)*x+final2[i][1]+(8+k2)*x+final2[i][2]+(8+k3)*x+final2[i][3])
pd.set_option("display.max_rows",None,"display.max.columns",None)
Residue_pair=[]
WT=[]
SP=[]
Change=[]
for j in range (len(final3)):
    Residue_pair.append(final3[j].split()[0])
    WT.append(final3[j].split()[1])
    SP.append(final3[j].split()[2])
    Change.append(float(final3[j].split()[3]))
Change=np.asarray(Change,float)
change=Change
Change=abs(Change)


df=pd.DataFrame({'Residue-Pair': Residue_pair,
                 '%system1': WT,
                 '%system2': SP,
                 '%system2-system1': change,
                 '%Change(absolute)': Change})
df1=df.sort_values(by=['%Change(absolute)'],ascending=False)
df1.drop(df1.columns[df.columns.str.contains('unnamed',case=False)],axis=1,inplace=True)
print(df1)


fo1.close()
fo2.close()
