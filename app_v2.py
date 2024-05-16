import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mp
import random 
import py3Dmol
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import AllChem

#Path to Separate complex info CSV
path_1 = "/Users/shahi.pra/Desktop/ppc_project/CSV_files/Separate complex info.csv"
#Lire le fichier Separate complex info csv 
df_ligands1 = pd.read_csv(path_1,sep=',')

#Path to Separate Lig info CSV
path_2 = "/Users/shahi.pra/Desktop/ppc_project/CSV_files/Separate ligand info.csv"
#Lire le fichier Separate Lig info CSV
df_ligands2 = pd.read_csv(path_2,sep=',')

#Path to metals info CSV
path_3 = "/Users/shahi.pra/Desktop/ppc_project/CSV_files/Metals_info.csv"
#Lire le fichier metals info CSV
df_ligands3 = pd.read_csv(path_3,sep=',')

### ENCADRÉ AU DESSUS DU COMPLEXE QUI TOURNE INDIQUANT SON ID ####
#function to display complex
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
        showmol(viewer, height = 500,width=1000)


#Générer un nbre aléatoire entre 0 et 60 800 
nombre_aleatoire = random.randint(0,60800)
print(nombre_aleatoire)

# Ce nombre correspond a la n-ieme ligne de SEPARATE COMPLEX INFO CSV et imprimer l'ID du complexe correspondant
complex_ID = df_ligands1.iloc[nombre_aleatoire,2]
print(complex_ID)

# 1) App : nom du complexe en haut du complexe qui tourne 
st.header(complex_ID)

# 2) Complexe qui tourne 
#ATTENTION AU NOM DU PATH !!!!! c'est le dossier tmQMg_xyz.zip extrait
#il tourne pas encore oups
display_molecule_from_xyz(rf"C:\peri_pc\cgc\ppc\project\tmQMg_xyz\{complex_ID}.xyz")

# 3) Bouton pour accéder aux ID de tous les complexes de la database --> bandeau déroulant les ID 
st.button("Reset", type="primary")
if st.button("Database", type="primary"):
   st.write(df_ligands1.iloc[:,2])
else:
    st.write()


# 4) User input le complexe qu'il cherche 
user_1 = st.text_input("🔎 ~ Tap a Complex ID", "")

######## Accès aux infos sur complexe choisi : user_1 ##############

# Création de 7 colonnes
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7 = st.columns(1)[0]


###0 : Trouver l'index et la colonne de l'élément
#ajout d'un test pour afficher un message d'erreur 
if user_1 != '' :   
    masque = df_ligands1.where(df_ligands1 == user_1)
    try: 
        index, colonne = masque.stack().index[0]
    except IndexError:
       st.write("Sorry, we do not know what this is...")
    index, colonne = masque.stack().index[0]


    ###1 : Afficher metal présent
    with col1:
        if st.button("Metals", type="secondary"):
            st.write(df_ligands1.iloc[index,8])


 ####3 : Afficher masse molaire du complexe
    with col2 :
        if st.button("Molar Mass", type="secondary"):
            st.write(df_ligands1.iloc[index,4])

    ####4 : Afficher Stoechiometry du complexe
    with col3:
        if st.button("Stoechiometry", type="secondary"):
            st.write(df_ligands1.iloc[index,7])
        
    ####5 : Afficher Nombre d'el du complexe
    with col4:
        if st.button("Number of electrons", type="secondary"):
            st.write(df_ligands1.iloc[index,6])


    ####6 : Afficher Nombre d'atomes du complexe
    with col5:
        if st.button("Number of atoms", type="secondary"):
            st.write(df_ligands1.iloc[index,5])

    #### 7 : Afficher charges du complexe
    with col6:
        if st.button("Charge", type="secondary"):
            st.write(df_ligands1.iloc[index,3])

    ####2 : Afficher les ligands du complexe sous forme de liste
    with col7:
        if st.button("Ligands", type="secondary"):
            st.write(df_ligands1.iloc[index,9])     # FREQ 
            x = (df_ligands1.iloc[index,9])
            liste = x.split("'")  
            ligands = []
            for i in range (0, (len(liste)-1)):
                if liste[i][0] == 'l' :
                    ligands.append(liste[i])
            st.write(str(ligands))              #SANS FREQUENCE
    #### EXTRA: AFFICHAGE DU COMPLEXE EN 3D
    display_molecule_from_xyz(rf"C:\peri_pc\cgc\ppc\project\tmQMg_xyz\{user_1}.xyz")
   

############ User_2 input le ligand qu'il cherche ########
user_2 = st.text_input("🔎 ~ Tap a Ligand ID", "")

###Accès aux infos sur le ligand choisi : user_2

# Création de 3 lignes
ligne1 = st.columns(1)
ligne2 = st.columns(3)
ligne3 = st.columns(1)

###0 : Trouver l'index et la colonne de l'élément
#ajout d'un test pour afficher un message d'erreur 
if user_2 != '':
    masque = df_ligands2.where(df_ligands2 == user_2)
    try: 
        index, colonne = masque.stack().index[0]
    except IndexError:
       st.write("Sorry, we do not know what this is...")
    index, colonne = masque.stack().index[0]

    ###1 : Afficher smiles
    if ligne1[0].button("SMILES", type="secondary"):
        ligne1[0].write(df_ligands2.iloc[index, 3])

    ###2 : Afficher stoechiometry
    if ligne2[0].button("STOECHIOMETRY", type="secondary"):
        ligne2[0].write(df_ligands2.iloc[index, 4])

    ###3 : Afficher charge
    if ligne2[1].button("CHARGE", type="secondary"):
        ligne2[1].write(df_ligands2.iloc[index, 5])

    ###4 : Afficher nombre d'atomes
    if ligne2[2].button("NUMBER OF ATOMS", type="secondary"):
        ligne2[2].write(df_ligands2.iloc[index, 6])

    ###5 : Afficher complexes
    if ligne3[0].button("COMPLEXES", type="secondary"):
        ligne3[0].write(df_ligands2.iloc[index, 7])

    ### extra: affichage du ligand en 3D
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
        return viewer
    ligand = MolTo3DView(smi2conf(df_ligands2.iloc[index, 3]), size=(600, 300))
    showmol(ligand)




###[theme]
#base="light"
#primaryColor="#0d602e"
#backgroundColor="#c6d6c5"
#font="serif"
