# CHARACTERISTICS DISPLAYED IN TABLES 

**Complex_info.csv** : this table displays the id, the charge, the molecular mass, the number of atoms, the stoechiometry and the the metal(s) appearing in every recorded complex. 
The last column contains the ligands appearing in each complex, as keys, alongside their number of occurance, as values. 
The raw database was sometimes incomplete. Therefore, some complex characteristics are missing.

**Metals_info.csv** : this table displays the *name*, *the molecular formula*, *the number of electrons* and *the number of valence of electrons* of each metal appearing in the periodic table.

**Ligands_info.csv** : this table displays the *id*, *the smiles*, *the stoechiometry*, *the charge and the number of atoms* in every recorded ligand. 
The last column conatins *the complex in which they appear* and *their number of appearances*.

**Coordinates_info.csv** : this table displays the *ligands* appearing in *each complex* alongside their *subgraphs*.
For each subgraph, the following file must be downloaded to obtain the coordinates of the atoms composing the studied subgraph :
https://github.com/hkneiding/tmQMg-L/blob/main/xyz/ligands_xyzs.xyz

**tmQMg_xyz** : this file contains *separate xyz info* for complexes in the database. It should be downloaded prior to running the application via this link: https://github.com/hkneiding/tmQMg/blob/main/data/tmQMg_xyz.zip and extracted into a file name tmQMg_xyz
