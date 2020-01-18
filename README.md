# Jupyter Notebook Tips and Tricks

A few (hopefully) useful tips and tricks to using the Jupyter Notebook with an eye to pragmatic usage. **This is not, in any way, an exhaustive demonstration of the features of the Jupyter notebook**. Further, you can go through these notebooks on your own, but I usually demonstrate using them and give lots of information verbally.

If you have any suggestions, edits, or corrections, please open an issue or let me know some other way. Best of luck!

## Assuming you are on a Mac

### Install Miniconda (if you haven't already)

```bash
cd ~/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
# go through the licensing and accept the defaults
source ~/.bashrc
conda update conda
```

### Create a new conda environments

The following commands are how I set up both my conda config and the enviroments that I use. 

Add conda-forge to your automatic channels, and the second line makes it so that you don't have to confirm that you want to install when you do things like `conda install numpy`.

```bash
conda config --add channels conda-forge
conda config --set always_yes yes
```

This following block is bash -- I recommend pasting in the commands one at a time to see what's happening.

```bash

# set the environment name here

envname='dspy3'

packages='
altair
anaconda-client
black
bqplot
ipyvolume
ipywebrtc
ipywidgets
jupyter
jupyter_contrib_nbextensions
jupyterlab
matplotlib
mkl
mpld3
notebook
numpy
pandas
pip
pivottablejs
pyparsing
pyscaffold
qgrid
scikit-learn
scipy
seaborn
sphinx
statsmodels
vaex
vega
vega_datasets
xlrd
yapf
'

conda create -n $envname python=3.6 $packages
conda activate $envname

# Pause here, double check that this pip is the correct one
type pip

# the correct one will say something like... 
# $ type pip
# pip is /Users/jonathan/miniconda3/envs/dspy3/bin/pip

python -m pip install pyhive[presto] sql_magic SQLAlchemy nbdime papermill

# lets the notebook extension (like ToC2) be enabled.
# Might not be needed!
# jupyter nbextension enable --py --sys-prefix widgetsnbextension

# This sets the name of the kernel that you want to select from the Kernel menu
python -m ipykernel install --user --name $envname --display-name "$envname"


# jupyterlab widgets
# conda install -c conda-forge nodejs  
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install ipyvolume jupyter-threejs @jupyterlab/toc
jupyter labextension install jupyter-threejs bqplot nbgather qgrid
```

### Troubleshooting

If you see an error message that says something about the iopub_data_rate_limit when you're trying to plot, try starting the notebook/lab with the following modified commands:

```bash
# Run to get a notebook
jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000

# Run to get lab
jupyter lab --NotebookApp.iopub_data_rate_limit=10000000

```

### Extra ideas

```bash
# create environment
conda env export -n dspy3 -f environment.lock.yaml
# load
conda env update --file environment.yaml

# to create new python package I did this from root directory of this repo
putup insight
cd insight/
python setup.py develop
```

