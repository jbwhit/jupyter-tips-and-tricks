
# coding: utf-8

# # Some Notebook Possibilities
# 
# http://mpld3.github.io/examples/linked_brush.html

# In[1]:

# uncomment the bottom line in this cell, change the final line of 
# the loaded script to `mpld3.display()` (instead of show).
# when it doesn't work, try to install mpld3 by: conda install mpld3
# when that fails: pip install mpld3, then rerun. :)
# %load http://mpld3.github.io/_downloads/linked_brush.py


# In[ ]:

# %load http://mpld3.github.io/_downloads/linked_brush.py
"""
Linked Brushing Example
=======================
This example uses the standard Iris dataset and plots it with a linked brushing
tool for dynamically exploring the data. The paintbrush button at the bottom
left can be used to enable and disable the behavior.
"""


# In[ ]:

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

import mpld3
from mpld3 import plugins, utils


# In[ ]:

data = load_iris()
X = data.data
y = data.target


# In[ ]:

# dither the data for clearer plotting
X += 0.1 * np.random.random(X.shape)


# In[2]:

fig, ax = plt.subplots(4, 4, sharex="col", sharey="row", figsize=(8, 8))
fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95,
                    hspace=0.1, wspace=0.1)

for i in range(4):
    for j in range(4):
        points = ax[3 - i, j].scatter(X[:, j], X[:, i],
                                      c=y, s=40, alpha=0.6)

# remove tick labels
for axi in ax.flat:
    for axis in [axi.xaxis, axi.yaxis]:
        axis.set_major_formatter(plt.NullFormatter())

# Here we connect the linked brush plugin
plugins.connect(fig, plugins.LinkedBrush(points))

# mpld3.show()
mpld3.display()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



