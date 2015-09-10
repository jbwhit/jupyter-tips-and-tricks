
# coding: utf-8

# # Pandas -- Love and Hate
# 
# If you've never used `pandas` before, it's amazing. It will also frustrate you to tears. 
# 
# High level tip -- try to represent data in the proper format: floats as floats; ints as ints; etc. Especially if you have dates, or timestamps, or datetimestamps, keep them in that format. The temptation to operate on them like strings may be overwhelming, but resist! In the long run you might prevail. :\

# In[1]:

# %install_ext http://raw.github.com/jrjohansson/version_information/master/version_information.py
get_ipython().magic(u'load_ext version_information')
get_ipython().magic(u'reload_ext version_information')
get_ipython().magic(u'version_information numpy, scipy, matplotlib, pandas')


# In[3]:

# Doing this in python 2.7 code allows for most of the code to be python 3 portable.
# But you have to write your print functions: print("Hello world.")
# from __future__ import division, absolute_import, print_function, unicode_literals
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')
sns.set_style('darkgrid') 
plt.rcParams['figure.figsize'] = 12, 8  # plotsize 


import numpy as np
import pandas as pd


# ### Note
# 
# Using cleaned data from [Data Cleaning](Data%20Cleaning.ipynb) Notebook. See Notebook for details.

# In[4]:

dframe = pd.read_csv("../data/coal_prod_cleaned.csv")


# ## Notebook Extensions -- qgrid

# In[5]:

# Check out http://nbviewer.ipython.org/github/quantopian/qgrid/blob/master/qgrid_demo.ipynb for more (including demo)
import qgrid # Best practices is to put imports at the top of the Notebook.
qgrid.nbinstall(overwrite=True)


# In[6]:

dframe.head()


# In[7]:

qgrid.show_grid(dframe[['MSHA_ID', 'Year', 'Mine_Name', 'Mine_State', 'Mine_County']], remote_js=True)


# In[8]:

plt.scatter(dframe.Average_Employees, dframe.Labor_Hours)
plt.xlabel("Number of Employees")
plt.ylabel("Total Hours Worked")


# In[9]:

plt.scatter(dframe.Labor_Hours, dframe.Production_short_tons, )
plt.xlabel("Total Hours Worked")
plt.ylabel("Total Amount Produced")


# In[10]:

colors = sns.color_palette(n_colors=11)


# In[11]:

color_dict = {key: value for key, value in zip(sorted(dframe.Year.unique()), colors)}


# In[12]:

color_dict


# In[13]:

for year in sorted(dframe.Year.unique()[[0,2, 5, -1]]):
    plt.scatter(dframe[dframe.Year == year].Labor_Hours,
                dframe[dframe.Year == year].Production_short_tons, 
                c=color_dict[year],
                s=50,
                label=year,
               )
plt.xlabel("Total Hours Worked")
plt.ylabel("Total Amount Produced")
plt.legend()
plt.savefig("ex1.png")


# In[ ]:

# facet grid


# In[14]:

for col in dframe.columns:
    print col


# In[ ]:




# # SQL connections
# 
# You will often use and interact with databases of some kind or another. Having the queries you ran to create the dataframes in a Notebook is great for future reference. There are many python/IPython connections to databases of all kinds: sqlite, mysql, impala, etc. 

# In[15]:

# An updated implementation from Christian Perez at SVDS https://github.com/cfperez/ipython-sql
get_ipython().magic(u'load_ext sql')
get_ipython().magic(u'reload_ext sql')


# In[16]:

coalproduction = dframe.copy()


# In[17]:

get_ipython().magic(u'config SqlMagic.autopandas=True')


# In[18]:

get_ipython().run_cell_magic(u'sql', u'sqlite://', u'PERSIST coalproduction')


# In[19]:

get_ipython().run_cell_magic(u'sql', u'sqlite://', u'SELECT DISTINCT company_type FROM coalproduction \nWHERE msha_id = 5000030')


# In[20]:

dbtest = get_ipython().magic(u'sql SELECT * FROM coalproduction')


# In[21]:

type(dbtest)


# In[22]:

dbtest.head()


# ## Use Cases for the Jupyter Notebook
# 
#  - Use Case 1: Teaching (Some basics to start!)
#  - Use Case 2: Exploratory Data Analysis
#  - Use Case 3: Running remotely (server)
#  - Use Case 4: Sharing results
#  - Use Case 5: Presentations
# 

# In[ ]:



