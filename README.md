# This code gives the difference in hydrogen bonding pattern between to similar systems.

# Installation:
  git clone https://github.com/KrishnenduSinha12/hb_network.git

# Required Input files:
   hbond-details.dat file for two systems using vmd
   pdb file of any one/both of the system

# Generated output file:
   Hb-details.dat: It contains all the pairs that show difference in hbond occupancy
   hb1.pml: It is a pymol script to visualise the change in h-bonding network

# How to use the code: 
   cd hb_network
   bash hbonding_network.sh 

# Changing the parameters:
   By default all the H-bond that show occupancy > 10 is reported. For changing the parameter open the hbonding_network.sh file and change the c parameter.
   If any non standard residue is present with 4 letters in your system you need to change it to a 3 letter residue name. for CYSG to CGR.
   By default the visualization shows only those pairs that have occupancy difference > 20. For changing the parameter open get_data.py file and change the cutoff value

# Bugs:
   This script doesn't add the Sidechain-Sidechain, Mainchain-Mainchain, and Mainchain-Sidechain interactions so when using, please take a look at the newly generated Hb-details.dat file. 
