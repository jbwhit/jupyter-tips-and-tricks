
# coding: utf-8

# # Github

# https://github.com/jbwhit/OSCON-2015/commit/6750b962606db27f69162b802b5de4f84ac916d5

# ## A few Python Basics

# Style Guide for Python Code: http://www.python.org/dev/peps/pep-0008/ 

# In[3]:

# Create a [list] 
days = ['Monday', # multiple lines 
        'Tuesday', # acceptable 
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday', 
       ] # trailing comma is fine!


# In[4]:

days


# In[5]:

# Simple for-loop
for day in days:
    print day


# In[6]:

# Double for-loop
for day in days:
    for letter in day:
        print letter,


# In[7]:

# Double for-loop
for day in days:
    for letter in day:
        print letter,
    print 


# In[8]:

for day in days:
    for letter in day:
        print letter.lower(), 


# ## List Comprehensions

# In[9]:

length_of_days = [len(day) for day in days]
length_of_days


# In[ ]:




# In[10]:

letters = [letter for day in days
                       for letter in day]


# In[12]:

letters = [letter for day in days for letter in day]
print letters 


# In[13]:

[num for num in xrange(10) if num % 2]


# In[14]:

[num for num in xrange(10) if num % 2 else "doesn't work"]


# In[15]:

[num if num % 2 else "works" for num in xrange(10)]


# In[16]:

sorted_letters = sorted([x.lower() for x in letters])
print sorted_letters


# In[17]:

unique_sorted_letters = sorted(set(sorted_letters))


# In[18]:

print "There are", len(unique_sorted_letters), "unique letters in the days of the week."
print "They are:", ''.join(unique_sorted_letters) 


# In[19]:

print "They are:", '; '.join(unique_sorted_letters) 


# In[20]:

def first_three(input_string):
    """Takes an input string and returns the first 3 characters."""
    return input_string[:3] 


# In[21]:

[first_three(day) for day in days]


# In[22]:

def last_N(input_string, number=2):
    """Takes an input string and returns the last N characters."""
    return input_string[-number:] 


# In[23]:

[last_N(day, 153) for day in days if len(day) > 6]


# In[24]:

from math import pi

print [str(round(pi, i)) for i in xrange(2, 9)] 


# In[27]:

list_of_lists = [[i, round(pi, i)] for i in xrange(2, 9)]
print list_of_lists


# In[29]:

for sublist in list_of_lists:
    print sublist


# In[30]:

# Let this be a warning to you!

# If you see python code like the following in your work:

for x in range(len(list_of_lists)):
    print "Decimals:", list_of_lists[x][0], 
    print "expression:", list_of_lists[x][1]
    


# In[31]:

# Change it to look more like this: 

for decimal, rounded_pi in list_of_lists:
    print "Decimals:", decimal, "expression:", rounded_pi
    
print list_of_lists


# In[32]:

# enumerate if you really need the index

for index, day in enumerate(days):
    print index, day


# ## Dictionaries
# 
# Python dictionaries are awesome. They are [hash tables](https://en.wikipedia.org/wiki/Hash_table) and have a lot of neat CS properties. Learn and use them well.

# In[33]:

from IPython.display import IFrame, HTML
HTML('<iframe src=https://en.wikipedia.org/wiki/Hash_table width=100% height=550></iframe>')


# In[34]:

fellows = ["Jonathan", "Zach", "Matt", "Wafa"]
sessions = ["2014-C", "2014-C", "2014-A", "2014-B"]


# In[35]:

dict(zip(fellows, sessions))


# In[36]:

insight = {fellow.lower(): session for fellow, session in zip(fellows, sessions)}


# In[37]:

insight


# In[38]:

# Standard Libraries
# collections; Counter, 
#


# In[39]:

insight['matt']


# In[40]:

rounded_pi = {i:round(pi, i) for i in xrange(2, 9)}


# In[41]:

rounded_pi[5]


# ## Participate in StackOverflow
# 
# An example: http://stackoverflow.com/questions/6605006/convert-pdf-to-image-with-high-resolution

# ## Julia Notebook
# 
# http://nbviewer.ipython.org/github/shashi/ijulia-notebooks/blob/master/funcgeo/Functional%20Geometry.ipynb

# # Extensions
# 
# https://github.com/ipython/ipython/wiki/Extensions-Index

# # R or Julia or Haskell or... SQL (get to that later)
# 
# You can use R as well -- I don't use it at all, so I took this small example below from http://nbviewer.ipython.org/github/ipython/ipython/blob/3607712653c66d63e0d7f13f073bde8c0f209ba8/docs/examples/notebooks/rmagic_extension.ipynb. 

# In[ ]:

# This broke!
# There are multiple extensions that allow for R to be executed, this is merely one of them
# I don't use it so I don't know if there's something better. 
# You have to install R as well. 
get_ipython().magic(u'load_ext rpy2.ipython')


# In[ ]:

X = np.array([0,1,2,3,4])
Y = np.array([3,5,4,6,7])


# In[ ]:

get_ipython().run_cell_magic(u'R', u'-i X,Y -o XYcoef', u'XYlm = lm(Y~X)\nXYcoef = coef(XYlm)\nprint(summary(XYlm))\npar(mfrow=c(2,2))\nplot(XYlm)')


# In[ ]:

FileLink("Overview.ipynb")

