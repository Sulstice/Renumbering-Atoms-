# Renumbering-Atoms-

 **Introduction**
  
 The goal of these scripts is for a quick way to renumber atoms in a Mol2 file based on a pattern of data to numbers the user desires.
 
 **How it works**
 In our data set we were fortunate to have a data set where every atom we wanted to renumber followed a unique pattern of O, H, H2, O. We    wanted to replace the the two oxygens to the same number in every molecule so we ran the docking we can say these two oxygens bind to this specific pocket as a constraint. 
 
 So we needed two functions (which can honestly be refactored to one script easily, which will be done soon) one that makes the switch of the data and one that sorts the respective numbers after so the docking simulation doesn't get the numbering all mixed up.
 
 **The Example Data Set**
 <p align="center">
  <img src="https://github.com/PellecchiaGroup/Renumbering-Atoms-/blob/master/Example.PNG" width="350"/>
</p>
 
 A time score was tallied up for our data set and it takes about 0.003 seconds per molecule. With our 97116 molecule data set it took 2.5 hours. 
 
The program efficiency is O(n squared)

**Todos**
  
- [] User can manually change in the code the atoms they would like to renumber
- [] User can search for a specific pattern and change the code
- [] Needs to be refactored to deal with high volume data
