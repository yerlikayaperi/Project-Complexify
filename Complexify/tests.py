import pytest
from rdkit import Chem
from module_3D import display_molecule_from_xyz, smi2conf, MolTo3DView

#testing display_molecule_from_xyz
@pytest.mark.parametrize("xyz_file", [
    "non_existent_file.xyz", #Test non-existent file
    "../Created Data/tmQMg_xyz/ABAFOZ.xyz", #Test valid file,
])

def test_display_molecule_from_xyz(xyz_file):
    with pytest.raises(FileNotFoundError):
        display_molecule_from_xyz(xyz_file)

def test_display_molecule_viewer_creation():
    viewer=display_molecule_from_xyz("valid_format.xyz")
    assert viewer is not None

#testing smi2conf
@pytest.mark.parametrize("smiles, expected_result", [
    ("CCO", Chem.Mol), #Valid SMILES
    ("INVALID_SMILES", None) #Invalid SMILES
    ])

def test_smi2conf_validity(smiles, expected_result):
    result = smi2conf(smiles)
    assert isinstance(result, expected_result)

def test_smi2conf_optimization():
    result=smi2conf("COO")
    assert result.GetConformer().Is3D()

#testing MolTo3DView
def test_MolTo3DView_valid_molecule():
    mol = Chem.MolFromSmiles("COO")
    viewer = MolTo3DView(mol)
    assert viewer is not None

def test_MolTo3DView_invalid_molecule():
    mol = None
    viewer = MolTo3DView(mol)
    assert viewer is None