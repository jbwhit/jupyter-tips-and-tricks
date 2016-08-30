# Jupyter Notebook Tips and Tricks

A few (hopefully) useful tips and tricks to using the Jupyter Notebook with an eye to pragmatic usage. **This is not, in any way, an exhaustive demonstration of the features of the Jupyter notebook**. Further, you can go through these notebooks on your own, but I usually demonstrate using them and give lots of information verbally.

If you have any suggestions, edits, or corrections, please open an issue or let me know some other way. Best of luck!

## Assuming you are on a Mac

### Install [homebrew](http://brew.sh/) (if you haven't already)

### Install Miniconda (if you haven't already)

```bash
cd ~/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
# go through the licensing 
source ~/.bashrc
```

### Create a few conda environments

```bash
conda config --add channels conda-forge

conda update conda

packages='astropy
ipywidgets
jupyter
jupyter_contrib_nbextensions
jupyter_nbextensions_configurator
matplotlib
mkl
mpld3
notebook
numpy
pandas
pip
pymc
pyparsing
scikit-learn
scipy
seaborn
statsmodels
'

conda create --name py2 python=2 $packages -y
conda create --name py3 python=3 $packages -y
# next 2 semi-experimental
conda create --name rpy3 -c r r-irkernel r-recommended r-essentials rpy2 python=3 $packages -y
conda create --name rpy2 -c r r-irkernel r-recommended r-essentials rpy2 python=2 $packages -y
# To run: 
source activate py2
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

