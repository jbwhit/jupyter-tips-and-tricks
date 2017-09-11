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

### Create a few conda environments

```bash

conda install anaconda-client
conda env create jbwhitmore/insightpy
source activate insightpy
ipython kernel install --display-name insightpy --name insightpy

# Run to get a notebook
jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000

# Run to get lab
jupyter lab --NotebookApp.iopub_data_rate_limit=10000000

```

