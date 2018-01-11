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


```bash
packages='jupyter
notebook
jupyterlab
jupyter_contrib_nbextensions
anaconda-client
ipywidgets
pyparsing
matplotlib
mkl
mpld3
seaborn
pip
pandas
scikit-learn
scipy
numpy
statsmodels
bqplot
pivottablejs
ipython-sql
ipyvolume'

conda create -n insightpy3 python=3 $packages
source activate insightpy3

# qgrid is currently on a tim_shawver's channel so get like so: 
conda install -c tim_shawver qgrid

# lets the notebook extension (like ToC2) be enabled.
jupyter nbextension enable --py --sys-prefix widgetsnbextension

# This sets the name of the kernel that you want to select from the Kernel menu
python -m ipykernel install --user --name insightpy3 --display-name "Insight Py3"


```

### Troubleshooting

If you see an error message that says something about the iopub_data_rate_limit when you're trying to plot, try starting the notebook/lab with the following modified commands:

```bash
# Run to get a notebook
jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000

# Run to get lab
jupyter lab --NotebookApp.iopub_data_rate_limit=10000000

```

