import numpy as np


f=open("HB2.dat","r")
p=f.readlines()
f.close()

print("set sphere_scale=0.45")
print("set sticks_transparency, 0.60")
print("select RhoA, resid 1-190")
print("select GDI,  resid 301-504")
print("color violetpurple , RhoA")
print("color teal, GDI")
#print("set sphere_color=yellow")
print("# set cartoon_color=violetpurple")
print("set cartoon_transparency, 0.70")
print("bg_color white")
print("set ray_opaque_background, on")
print("set defer_builds_mode, 4")
print("set label_size,20")

print("\n")

for i in range (1,len(p)):
    if float(p[i].split()[6]) > 15:
        if float(p[i].split()[5]) > 0:
            print ("select a," + " " + "resid" + " " + str(p[i].split()[1][3:6])+ " " +" and " +"name CA")
            print ("select b," + " " + "resid" + " " + str(p[i].split()[2][3:6])+ " " +" and " +"name CA")
            print ("show spheres, a")
            print ("show spheres, b_")
            print ("label a , oneletter+resi")
            print ("label b_, oneletter+resi")
            print("distance"+ " d1 , a, b_")
            print("hide labels," " d1")
            print("set dash_color, blue, d1")
        else:
            print ("select a," + " " + "resid" + " " + str(p[i].split()[1][3:6])+ " " +" and " +"name CA")
            print ("select b," + " " + "resid" + " " + str(p[i].split()[2][3:6])+ " " +" and " +"name CA")
            print ("show spheres, a")
            print ("show spheres, b_")
            print ("label a, oneletter+resi")
            print ("label b_, oneletter+resi")
            print("distance"+ " d2 , a, b_")
            print("hide labels," " d2")
            print("set dash_color, red, d2")
        
        print("\n")
p1=[]
p2=[]
for i in range (1,len(p)):
    p1.append(p[i].split()[1][3:6])
    p2.append(p[i].split()[2][3:6])

f_open=open("mindist_input.dat","w")

for j in range (len(p1)):
    f_open.write(str(p1[j])+" "+str(p2[j])+"\n")
f_open.close()
