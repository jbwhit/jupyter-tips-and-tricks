
# coding: utf-8

# # Jupyter Notebook Basics 

# In[1]:

names = ['alice', 'jonathan', 'bobby']
ages = [24, 32, 45]
ranks = ['kinda cool', 'really cool', 'insanely cool']


# In[3]:

for (name, age, rank) in zip(names, ages, ranks):
    print name, age, rank


# In[4]:

for index, (name, age, rank) in enumerate(zip(names, ages, ranks)):
    print index, name, age, rank


# In[5]:

# return, esc, shift+enter, ctrl+enter
# text keyboard shortcuts -- cmd > (right), < left,
# option delete (deletes words)
# type "h" for help
# tab
# shift-tab
# keyboard shortcuts
#  - a, b, y, m, dd, h, ctrl+shift+-


# In[14]:

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u"config InlineBackend.figure_format='retina'")

import matplotlib.pyplot as plt
# no pylab
import seaborn as sns
sns.set_context('talk')
sns.set_style('darkgrid') 
plt.rcParams['figure.figsize'] = 12, 8  # plotsize 

import numpy as np
# don't do `from numpy import *`
import pandas as pd


# In[9]:

# If you have a specific function that you'd like to import
from numpy.random import randn


# In[10]:

x = np.arange(100)
y = np.sin(x)
plt.plot(x, y)#;


# In[12]:

get_ipython().magic(u'matplotlib notebook')


# In[13]:

x = np.arange(10)
y = np.sin(x)
plt.plot(x, y)#;


# ## Magics!
# 
#  - % and %% magics
#  - interact
#  - embed image
#  - embed links, youtube
#  - link notebooks

# Check out http://matplotlib.org/gallery.html select your favorite.

# In[15]:

get_ipython().run_cell_magic(u'bash', u'', u'for num in {1..5}\ndo\n    for infile in *;\n    do\n        echo $num $infile\n    done\n    wc $infile\ndone')


# In[20]:

print "hi"
get_ipython().system(u'pwd')


# In[17]:

get_ipython().system(u'ping google.com')


# In[18]:

this_is_magic = "Can you believe you can pass variables and strings like this?"


# In[22]:

hey = get_ipython().getoutput(u'echo $this_is_magic')


# In[23]:

hey


# # Numpy 
# 
# If you have arrays of numbers, use `numpy` or `pandas` (built on `numpy`) to represent the data. Tons of very fast underlying code.

# In[24]:

x = np.arange(10000)

print x  # smart printing


# In[25]:

print x[0] # first element 
print x[-1] # last element
print x[0:5] # first 5 elements (also x[:5])
print x[:] # "Everything"


# In[26]:

print x[-5:] # last five elements


# In[27]:

print x[-5:-2]


# In[28]:

print x[-5:-1] # not final value -- not inclusive on right


# In[ ]:




# In[29]:

x = np.random.randint(5, 5000, (3, 5))


# In[30]:

x


# In[31]:

np.sum(x)


# In[32]:

x.sum()


# In[42]:

np.sum(x)


# In[41]:

np.sum(x, axis=0)


# In[43]:

np.sum(x, axis=1)


# In[44]:

x.sum(axis=1)


# In[45]:

# Multi dimension array slice with a comma
x[:, 2]


# In[ ]:




# In[46]:

y = np.linspace(10, 20, 11)
y


# In[47]:

get_ipython().magic(u'pinfo np.linspace')


# In[ ]:

np.linspace()
# shift-tab; shift-tab-tab
np.


# In[48]:

def does_it(first=x, second=y):
    """This is my doc"""
    pass


# In[49]:

y[[3, 5, 7]]


# In[ ]:

does_it()


# In[51]:

num = 3000
x = np.linspace(1.0, 300.0, num)
y = np.random.rand(num)
z = np.sin(x)
np.savetxt("example.txt", np.transpose((x, y, z)))


# In[52]:

get_ipython().magic(u'less example.txt')


# In[53]:

get_ipython().system(u'wc example.txt')


# In[54]:

get_ipython().system(u'head example.txt')


# In[55]:

#Not a good idea
a = []
b = []
for line in open("example.txt", 'r'):
    a.append(line[0])
    b.append(line[2])
    
a[:10] # Whoops! 


# In[56]:

a = []
b = []
for line in open("example.txt", 'r'):
    line = line.split()
    a.append(line[0])
    b.append(line[2])
    
a[:10] # Strings! 


# In[57]:

a = []
b = []
for line in open("example.txt", 'r'):
    line = line.split()
    a.append(float(line[0]))
    b.append(float(line[2]))
    
a[:10] # Lists!


# In[58]:

# Do this!
a, b = np.loadtxt("example.txt", unpack=True, usecols=(0,2))


# In[59]:

a


# ## Matplotlib and Numpy 
# 

# In[60]:

from numpy.random import randn


# In[61]:

num = 50
x = np.linspace(2.5, 300, num)
y = randn(num)
plt.scatter(x, y)


# In[64]:

y > 1


# In[65]:

y[y > 1]


# In[66]:

y[(y < 1) & (y > -1)]


# In[67]:

plt.scatter(x, y, c='b', s=50)
plt.scatter(x[(y < 1) & (y > -1)], y[(y < 1) & (y > -1)], c='r', s=50)


# In[68]:

y[~((y < 1) & (y > -1))] = 1.0
plt.scatter(x, y, c='b')
plt.scatter(x, np.clip(y, -0.5, 0.5), color='red')


# In[71]:

num = 350
slope = 0.3
x = randn(num) * 50. + 150.0 
y = randn(num) * 5 + x * slope
plt.scatter(x, y, c='b')


# In[72]:

# plt.scatter(x[(y < 1) & (y > -1)], y[(y < 1) & (y > -1)], c='r')
# np.argsort, np.sort, complicated index slicing
dframe = pd.DataFrame({'x': x, 'y': y})
g = sns.jointplot('x', 'y', data=dframe, kind="reg")


# ## Grab Python version of ggplot http://ggplot.yhathq.com/

# In[73]:

from ggplot import ggplot, aes, geom_line, stat_smooth, geom_dotplot, geom_point


# In[74]:

ggplot(aes(x='x', y='y'), data=dframe) + geom_point() + stat_smooth(colour='blue', span=0.2)


# In[ ]:



