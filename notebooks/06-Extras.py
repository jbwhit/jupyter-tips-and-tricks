
# coding: utf-8

# ## Learn the standard library to at least know what's there
# 
# ### itertools and collections have very useful features
# 
#  - chain
#  - product
#  - permutations
#  - combinations
#  - izip

# In[1]:

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u"config InlineBackend.figure_format='retina'")

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')
sns.set_style('darkgrid') 
plt.rcParams['figure.figsize'] = 12, 8  # plotsize 

import numpy as np
import pandas as pd


# In[2]:

# plot residuals


# In[3]:

from itertools import groupby # NOT REGULAR GROUPBY
from itertools import product, cycle, izip
import re # regular expressions


# ## Challenge (Easy)
# 
# Write a function to return the total number of digits in a given string, and those digits. 

# In[5]:

test_string = """de3456yghj87654edfghuio908ujhgyuY^YHJUi8ytgh gtyujnh y7"""


# In[6]:

count = 0
digits = []
for x in test_string:
    try: 
        int(x)
        count += 1
        digits.append(int(x))
    except:
        pass
    
print "Number of digits:", str(count) + ";"
print "They are:", digits


# ## Challenge (Tricky)
# 
# Same as above -- but were consecutive digits are available, return as a single number. 
# 
# Ex. "2a78b123" returns "3 numbers, they are: 2, 78, 123"

# In[7]:

test_string


# In[8]:

groups = []
uniquekeys = []
for k, g in groupby(test_string, lambda x: x.isdigit()):
    groups.append(list(g))
    uniquekeys.append(k) 


# In[9]:

print(groups)
print(uniquekeys)


# In[10]:

numbers = []
for x, y in izip(groups, uniquekeys):
    if y:
        numbers.append(int(''.join([j for j in x])))
print "Number:", np.sum(uniquekeys)
print "They are:", numbers


# In[11]:

# In one cell

def solution_2(test_string):
    groups = []
    uniquekeys = []
    for k, g in groupby(test_string, lambda x: x.isdigit()):
        if k:
            groups.append(int(''.join([j for j in g])))

    return len(groups), groups
    
print solution_2(test_string) 


# ## Challenge (Tricky)
# 
# Same as above, but do it a second way.
# 

# In[12]:

def solution_3(test_string):
    """Regular expressions can be a very powerful and useful tool."""
    groups = [int(j) for j in re.findall(r'\d+', test_string)]
    return len(groups), groups

solution_3(test_string)


# ## Challenge (Hard)
# 
# Same as above, but all valid numbers expressed in digits, commas, and decimal points. 
# 
# Ex. "a23.42dx9,331nm87,55" -> 4; 23.42, 9331, 87, 55
# 
# Left as an exercise :) 
# 
# Don't spend much time on this one.

# ## Generators

# In[13]:

def ex1(num):
    """A stupid example generator to prove a point."""
    while num > 1:
        num += 1
        yield num 


# In[14]:

hey = ex1(5)


# In[15]:

hey.next()


# In[58]:

hey.next()


# # Gotchas
# 
# Modifying a dictionary's keys while iterating over it. 
# 
# ```python
# for key in dictionary:
#     if key == "bat":
#         del dictionary[key]
# ```
# 
# If you have to do something like this: 
# 
# ```python
# list_of_keys = dictionary.keys()
# for key in list_of_keys:
#     if key == "bat":
#         del dictionary[key]
# ```

# In[ ]:



