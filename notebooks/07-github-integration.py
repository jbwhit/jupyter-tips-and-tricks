
# coding: utf-8

# In[ ]:

# %install_ext https://raw.githubusercontent.com/rasbt/watermark/master/watermark.py
get_ipython().magic(u'load_ext watermark')
get_ipython().magic(u'watermark --githash --machine --python --packages pandas,numpy,matplotlib -u --custom_time %Y-%m-%d')


# https://github.com/jbwhit/OSCON-2015/commit/6750b962606db27f69162b802b5de4f84ac916d5

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import seaborn as sns
sns.set();


# In[ ]:

x = np.random.random_sample(1000) * 50.0


# In[ ]:

y = np.sin(x)


# In[ ]:

plt.scatter(x, y)


# In[ ]:

# Create new visualization


# In[ ]:

plt.scatter(x ** 2.0,y**2.0, color='red')


# In[ ]:

plt.scatter(x,y**2.0, color='red')


# In[ ]:




# In[ ]:



