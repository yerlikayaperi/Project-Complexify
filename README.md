![Project Logo](assets/readmebanner.jpg)

![Coverage Status](https://raw.githubusercontent.com/pschwllr/minimal_project/main/assets/coverage-badge.svg)

<h1 align="center">
Coordination Complex Database
</h1>

<br>


Code for a streamlit page created for users wishing to navigate databases tmqm, tmQmg and tmQmg-L more easily.

## 🔥 Usage

> Provides the metal, molar mass, stoechiometry, number of electrons, charge and ligands of over 60 000 coordination complexes ! 
> Also gives over 30 000 ligands' SMILES, stoechiometry, charge, number of atoms and complexes they can be found in !
> All complexes and ligands are shown in 3D with the help of py3Dmol.


## 👩‍💻 Installation

Create a new environment, you may also give the environment a different name. 

```
conda create -n complexify python=3.10 
```

```
conda activate complexify
```

If you need jupyter lab, install it 

```
(complexify) $ pip install jupyterlab
```

## Pre-required modules

For this project to work, the following extensions are automatically downloaded during the pip install:
  - streamlit
  - rdkit
  - py3Dmol
  - numpy
  - pandas
  - stmol
  - matplotlib


## 🛠️ Development installation

Initialize Git (only for the first time). 

```
git init
git add * 
git add .*
git commit -m "Initial commit" 
git branch -M main
git remote add origin git@github.com:yerlikayaperi/Project_Complexify.git 
git push -u origin main
```

Then add and commit changes as usual. 

🔺  **Before installing the package, please download in the Created Data file of the repository the following two files:** 🔺
- **ligands_xyzs.xyz** : https://github.com/hkneiding/tmQMg-L/blob/main/xyz/ligands_xyzs.xyz
- **tmQMg_xyz.zip** : https://github.com/hkneiding/tmQMg/blob/main/data/tmQMg_xyz.zip which should be extracted in a file named tmQMg_xyz in the Created Data file

To install the package, run in the repository 

```
(complexify) $ cd Complexify
(complexify) $ python setup.py sdist bdist_wheel
(complexify) $ cd dist
(complexify) $ pip install complexify-1.0.0.tar.gz
(complexify) $ cd ..
(complexify) $ streamlit run complexify_app.py  
```

The last two lines will launch the application in your browser.

### Run tests and coverage

```
(conda_env) $ pip install tox
(conda_env) $ tox
```

### Generate coverage badge

Works after running `tox`

```
(conda_env) $ pip install "genbadge[coverage]"
(conda_env) $ genbadge coverage -i coverage.xml
```

Generated with some inspiration from [cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) and [copier-pylib](https://github.com/astrojuanlu/copier-pylib).


