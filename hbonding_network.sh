# This script will create a input file for pymol to visualize H-bonding network in a protein



python Hb-details.py -f1 /home/krishnendu/Downloads/holo_hbonds-details.dat -f2 /home/krishnendu/Downloads/apo_hbonds-details.dat -c 25  > HB_details1.dat

sed "s/-Main/     /g" HB_details1.dat > HB2.dat
sed -i "s/-Side/     /g" HB2.dat
sed -i "s/--/  /g" HB2.dat
sed -i "s/CYSG/CGR/g" HB2.dat


python get_data.py > hb1.pml

rm -rf HB2.dat
 


