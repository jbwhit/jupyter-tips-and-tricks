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
```

### Create a few conda environments

```bash

conda update conda
# This adds the conda-forge channel below the defaults library
conda config --append channels conda-forge

packages='jupyter
notebook
ipywidgets
jupyter_contrib_nbextensions
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
tqdm'

conda create -q --name py2 python=2 $packages
# Only including r in py3 because conda install r and py2 don't work.
# If you need it, force
conda create --name insightpy3 --channel r r r-irkernel r-recommended r-essentials rpy2 python=3 $packages -y

source activate insightpy3
# Install the matplotlib style library
# https://github.com/ipython/ipython/issues/8873#issuecomment-146185652
ipython kernel install --display-name insightpy3 --name insightpy3
```

### Fancy unnecessary stuff

Add this (modify it first) to your `.bashrc`

```bash
export initials='jbw'

minimalnb () {
    # Usage: minimalnb [exploratory_data_analysis]
    # Will download the most up-to-date minimal notebook named with:
    # today's date, your initials, and [an optional phrase].
    # The example would yield a file in the current directory named: 
    # 2016-08-17_jbw_exploratory_data_analysis.ipynb
    curl -H 'Accept: application/vnd.github.v3.raw' -L \
    https://api.github.com/repos/jbwhit/jupyter-tips-and-tricks/contents/templates/minimal.ipynb \
    -o `date +%Y-%m-%d`_${initials}_$1.ipynb
} 
```

```
jupyter nbextension enable --py --sys-prefix widgetsnbextension
ipython kernel install --display-name insightpy3 --name insightpy3
```
