# Renumbering-Atoms-

 **Introduction**
  
  Here is demonstrated a set of two scripts, one for renumbering and one for sorting. The goal of these scrips is to take in a big dataset of peptide molecules in a mol2 format and renumber the atoms and sort after renumbering to set specific atom constraints in docking simulations. 
 
 **How it works**
 
 So using fragment based discovery we were able to predict that the functional group hydroxylamine was able to bind into the binding of our protein. So knowing that we began to construct the rest of the molecule with this core foundation built into. 
 
 <p align="center">
  <img src="https://github.com/PellecchiaGroup/Renumbering-Atoms-/blob/master/Hydroxylamine.png" width="350"/>
</p>
 
 In our computational data we have two examples of using these scripts too acomplish the specific renumbering. Two patterns of data of O, H, H2, O  and O, N, H, O. In both cases we wanted the oxygens to bind into the core structure for activity. To set this constraint we can set the atom numbers to bind into a specific region. The problem associated with this was that these mol2 files have 97,116 molecules confided in one file and each molecule has a varying length which poses as a problem for the numbering because each atom is a different number. 
 
The first python code takes in the data file and looks for the specific pattern we implemented for the core functional group
 
 #Pattern Number 1
 <p align="center">
  <img src="https://github.com/PellecchiaGroup/Renumbering-Atoms-/blob/master/Example.PNG" width="350"/>
</p>
 
 #Pattern Number 2
 <p align="center">
  <img src="https://github.com/PellecchiaGroup/Renumbering-Atoms-/blob/master/AcidExample.PNG" width="350"/>
</p>

Next we renumber the atoms that we care for, in our case the two oxygens and renumber them to 7 and 8 respectively and swapped the numbers that were originally the two oxygen numbers. 

 <p align="center">
  <img src="https://github.com/PellecchiaGroup/Renumbering-Atoms-/blob/master/LineCodePattern.PNG" width="350"/>
</p>

Or the similiar pattern demonstrated before in Pattern Number 2 and renumbers the atoms. After that our sorting code ran through and resorted the atoms.

A quick solution to renumbering atoms of interested based on patterns of data. Manually changing 97,116 molecules by hand for us would be tedious so a quick script remedies that.

A time score was tallied up for our data set and it takes about 0.003 seconds per molecule. With our 97116 molecule data set it took 2.5 hours. 
 
The program efficiency is O(n squared)

**Todos**
  
- [] User can manually change in the code the atoms they would like to renumber
- [] Program needs to find a pattern of data similiar and make recommendations
- [] Needs to be refactored to deal with high volume data
