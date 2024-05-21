import re
import py3Dmol
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import AllChem


def display_molecule_from_xyz(xyz_file):
    """
    Draw molecule in 3D from its xyz coordinate file
    
    Args:
    ---
    xyz_file: .xyz, coordinates of molecule to show
    Return:
    ---
    showmol(viewer, height = 500,width=1000) : 3D visual of molecule that spins on itself

    """
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

def smi2conf(smiles):
        '''
        Convert SMILES to rdkit.Mol with 3D coordinates
        Args:
        ---
        smiles: string, SMILES of molecule
        Return:
        ---
        mol: rdkit.Mol, molecule to show
        OR
        None: bool, if mol could not be found/is incorrect
        '''
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
    
