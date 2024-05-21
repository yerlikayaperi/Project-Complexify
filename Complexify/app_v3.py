import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mp
import random 
import py3Dmol
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import AllChem
import base64
import ast

#Path to Complex_info.csv
path_1 = "../Created Data/Complex_info.csv"
#Read the file correctly
df_ligands1 = pd.read_csv(path_1,sep=',')

#Path to Ligands_info.csv
path_2 = "../Created Data/Ligands_info.csv"
#Read the file correctly
df_ligands2 = pd.read_csv(path_2,sep=',')

#Path to Metals_info.csv
path_3 = "../Created Data/Metals_info.csv"
#Read the file correctly
df_ligands3 = pd.read_csv(path_3,sep=',')

#Path to Coordinates_info.csv
path_4 = "../Created Data/Coordinates_info.csv"
#Read the file correctly
df = pd.read_csv(path_4,sep=',')

# Path to ligands_xyzs 
chemin_fichier = "../Created Data/ligands_xyzs.xyz"


#Generate a random number between 0 and 60 800 
nombre_aleatoire = random.randint(0,60800)
print(nombre_aleatoire)

# This function displays a rotating complex in 3D 
def display_molecule_from_xyz(xyz_file):
    with open(xyz_file, 'r') as f:
        coordinates=''
        lines=f.readlines()
        for line in lines:
                coordinates= coordinates + str(line)
        viewer=py3Dmol.view(width=1000,height=500)
        #viewer.setViewStyle({"style": "outline", "width": 0.01})
        viewer.addModel(coordinates)
        # visualize with the sticks and spheres
        viewer.setStyle({"stick":{},"sphere": {"scale":0.25}})
        #viewer.animate()
        viewer.zoomTo()
        viewer.spin()
        showmol(viewer, height = 500,width=1000)


# Display the random complex name at the top of the rotating complex 
complex_ID = df_ligands1.iloc[nombre_aleatoire,2]
st.header(complex_ID)


#ATTENTION AU NOM DU PATH !!!!! c'est le dossier tmQMg_xyz.zip extrait


display_molecule_from_xyz(rf"..\Created Data\tmQMg_xyz\{complex_ID}.xyz")



# This button indicates all the complexes ID of the database tmQMg_properties_and_targets.csv
st.button("Reset", type="primary")
if st.button("Database", type="primary"):
   st.write(df_ligands1.iloc[:,2])
else:
    st.write()


# The user inputs the ID complex for which he wants to know its characteristics 
user_1 = st.text_input("🔎 ~ Tap a Complex ID", "")


# Creation of 8 columns for a good display 
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7 = st.columns(1)[0]
col8 = st.columns(1)[0]


#Dictionnary xyzs found on https://github.com/hkneiding/tmQMg-L to associate the COMPLEX-subgraph to the xyz coordinates of the ligands' atoms
xyzs = {}
with open(chemin_fichier, 'r') as fh:
    for xyz in fh.read().split('\n\n'):
        cle = xyz.split('\n')[1].replace('\n', ';')  # Remplacer les '\n' par des ';'
        valeur = xyz.replace('\n', '; ')  # Remplacer les '\n' par des ';'
        xyzs[cle] = valeur


#Print a message error if the user's input is not found 
if user_1 != '' :   
    masque = df_ligands1.where(df_ligands1 == user_1)
    try: 
        index, colonne = masque.stack().index[0]
    except IndexError:
       st.write("Sorry, we do not know what this is...")
    index, colonne = masque.stack().index[0]


    ###1 : Display the metal appearing in the complex (user_1)
    with col1:
        if st.button("Metal", type="secondary"):
            st.write(df_ligands1.iloc[index,8])

    
    ####2 : Display the ligands appearing in the complex (user_1) as a list with the number of occurences 
    with col7:
        if st.button("Ligands", type="secondary"):
            st.write(df_ligands1.iloc[index,9])     
            x = (df_ligands1.iloc[index,9])
            liste = x.split("'")  
            ligands = []
            for i in range (0, (len(liste)-1)):
                if liste[i][0] == 'l' :
                    ligands.append(liste[i])
            

    
    #display the complex (user_1)
    display_molecule_from_xyz(rf"../Created Data/tmQMg_xyz/{user_1}.xyz")



    ####3 : Display the molar mass of the complex (user_1)
    with col2 :
        if st.button("Molar Mass", type="secondary"):
            st.write(df_ligands1.iloc[index,4])

    ####4 : Display the Stoechiometry of the complex (user_1)
    with col3:
        if st.button("Stoechiometry", type="secondary"):
            st.write(df_ligands1.iloc[index,7])
        
    ####5 : Display the number of electrons of the complex (user_1)
    with col4:
        if st.button("Number of electrons", type="secondary"):
            st.write(df_ligands1.iloc[index,6])


    ####6 :Display the number of atoms of the complex (user_1)
    with col5:
        if st.button("Number of atoms", type="secondary"):
            st.write(df_ligands1.iloc[index,5])

    ####7 : Display the charge of the complex (user_1)
    with col6:
        if st.button("Charge", type="secondary"):
            st.write(df_ligands1.iloc[index,3])


    ####8 : For the complex (user_1), display each atoms' coordinates for each ligand 
    with col8:
        if st.button("Coordinates"):
            liste = ast.literal_eval(df.iloc[index,1])  
    
            ligands = []
            lig = 0
            complex_subgraph = []
            coord = []

            for element in liste:
                if element.startswith('ligand'):
                    ligands.append(element)
                elif element.startswith(f'{user_1}-subgraph'):
                    complex_subgraph.append(element)
                    
            for element in liste:
                for cle in xyzs.keys():
                    
                    if cle == element:
                        coord.append(xyzs[cle][22:])
            print(coord)
            print(complex_subgraph)
            print(ligands)
 
            dfxyz = pd.DataFrame({'Ligands subgraph': complex_subgraph,'Coordinates of each atom of the subgraph (xyz)': coord})
            dfxyz['Coordinates of each atom of the subgraph (xyz)'] = dfxyz['Coordinates of each atom of the subgraph (xyz)'].str.replace(';', '<br>')
            st.write(dfxyz.to_html(escape=False), unsafe_allow_html=True)

            
   

# The user inputs the ligand ID for which he wants to know its characteristics 
user_2 = st.text_input("🔎 ~ Tap a Ligand ID", "")


# Creation of 3 columns for a good display 
ligne1 = st.columns(1)
ligne2 = st.columns(3)
ligne3 = st.columns(1)


#Print a message error if the user's input is not found 
if user_2 != '':
    masque = df_ligands2.where(df_ligands2 == user_2)
    try: 
        index, colonne = masque.stack().index[0]
    except IndexError:
       st.write("Sorry, we do not know what this is...")
    index, colonne = masque.stack().index[0]

    ###1 : Display the smiles of the ligand (user_2)
    if ligne1[0].button("SMILES", type="secondary"):
        ligne1[0].write(df_ligands2.iloc[index, 3])

    ###2 : Display the stoechiometry of the ligand (user_2)
    if ligne2[0].button("STOECHIOMETRY", type="secondary"):
        ligne2[0].write(df_ligands2.iloc[index, 4])

    ###3 : Display the charge of the ligand (user_2)
    if ligne2[1].button("CHARGE", type="secondary"):
        ligne2[1].write(df_ligands2.iloc[index, 5])

    ###4 : Display the number of atoms of the ligand (user_2)
    if ligne2[2].button("NUMBER OF ATOMS", type="secondary"):
        ligne2[2].write(df_ligands2.iloc[index, 6])

    ###5 : Display the complexes in which the ligand (user_2) appear
    if ligne3[0].button("COMPLEXES", type="secondary"):
        ligne3[0].write(df_ligands2.iloc[index, 7])

    ### Display the ligand (user_2) in 3D
    def smi2conf(smiles):
        '''Convert SMILES to rdkit.Mol with 3D coordinates'''
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            mol = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol)
            AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
            return mol
        else:
            return None
    def MolTo3DView(mol, size=(300, 300), style="stick", surface=False, opacity=0.5):
        """Draw molecule in 3D
    
    Args:
    ----
        mol: rdMol, molecule to show
        size: tuple(int, int), canvas size
        style: str, type of drawing molecule
               style can be 'line', 'stick', 'sphere', 'carton'
        surface, bool, display SAS
        opacity, float, opacity of surface, range 0.0-1.0
    Return:
    ----
        viewer: py3Dmol.view, a class for constructing embedded 3Dmol.js views in ipython notebooks.
    """
        assert style in ('line', 'stick', 'sphere', 'cartoon')
        mblock = Chem.MolToMolBlock(mol)
        viewer = py3Dmol.view(width=size[0], height=size[1])
        viewer.addModel(mblock, 'mol')
        viewer.setStyle({"stick":{},"sphere": {"scale":0.25}})
        if surface:
            viewer.addSurface(py3Dmol.SAS, {'opacity': opacity})
        viewer.zoomTo()
        viewer.spin()
        return viewer
    ligand = MolTo3DView(smi2conf(df_ligands2.iloc[index, 3]), size=(600, 300))
    showmol(ligand)




###[theme]
#base="light"
#primaryColor="#0d602e"
#backgroundColor="#c6d6c5"
#font="serif"