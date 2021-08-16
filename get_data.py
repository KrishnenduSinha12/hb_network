import numpy as np


f=open("HB2.dat","r")
p=f.readlines()
f.close()

print("set sphere_scale=0.35")
print("set sphere_color=yellow")
print("set cartoon_color=violetpurple")
print("set cartoon_transparency, 0.75")
print("bg_color white")
print("set ray_opaque_background, off")
print("set defer_builds_mode, 4")


print("\n")

cutoff=20

for i in range (1,len(p)):
    if float(p[i].split()[6]) > cutoff:
        if float(p[i].split()[5]) > 0:
            print ("select a," + " " + "resid" + " " + str(p[i].split()[1][3:6])+ " " +" and " +"name CA")
            print ("select b," + " " + "resid" + " " + str(p[i].split()[2][3:6])+ " " +" and " +"name CA")
            print ("show spheres, a")
            print ("show spheres, b_")
            print ("label a , oneletter+resi")
            print ("label b_, oneletter+resi")
            print("distance"+ " d1 , a, b_")
            print("hide labels," " d1")
            print("set dash_color, red, d1")
        else:
            print ("select a," + " " + "resid" + " " + str(p[i].split()[1][3:6])+ " " +" and " +"name CA")
            print ("select b," + " " + "resid" + " " + str(p[i].split()[2][3:6])+ " " +" and " +"name CA")
            print ("show spheres, a")
            print ("show spheres, b_")
            print ("label a, oneletter+resi")
            print ("label b_, oneletter+resi")
            print("distance"+ " d2 , a, b_")
            print("hide labels," " d2")
            print("set dash_color, blue, d2")
        
        print("\n")

