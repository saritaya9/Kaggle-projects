
# coding: utf-8

# In[2]:

import pandas as pd

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

s1 = pd.Series(sdata)

s1


# In[9]:

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

DF1 = pd.DataFrame(data)
print(DF1)


# In[11]:

DF2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four', 'five'])
print(DF2)


# In[20]:

DF2[['year','state','debt']]

DF2['year']


# In[31]:

DF2.ix['two']


# In[32]:

DF2['debt'] = 16.5
print(DF2)


# In[33]:

DF2['debt'] = [16.5,7.5,20.6,8,3]
print(DF2)


# In[35]:

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
print(val)
DF2['debt'] = val

print(DF2)


# In[36]:

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

DF3 = pd.DataFrame(pop)

print(DF3)


# In[37]:

print(DF3.T)


# In[40]:

import numpy as np
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

print(obj)


# In[43]:

obj1= obj.drop('b')

print(obj1)


# In[45]:

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])


# In[47]:

print(obj)


# In[49]:

obj['b']


# In[51]:

obj[[1,3]]


# In[52]:

obj[obj<2]


# In[53]:

obj['b':'c'] = 5
print(obj)


# In[57]:

data =pd.DataFrame(np.arange(16).reshape((4, 4)),
        index=['Ohio', 'Colorado', 'Utah', 'New York'],
        columns=['one', 'two', 'three', 'four'])
print(data)


# In[59]:

data[['three','one']]


# In[60]:

data[:2]


# In[61]:

data[data['three']<5]


# In[62]:

print('one','two','three','four')


# In[66]:

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd','e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g']) 
print(s1)
print(s2)


# In[68]:

s3 = s1+s2
print(s3)


# In[69]:

L1 = list('bcd')
print(L1)


# In[71]:

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
      index=['Ohio', 'Texas', 'Colorado'])
print(df1)


# In[ ]:



