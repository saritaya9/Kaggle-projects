
# coding: utf-8

# In[3]:

import numpy as np
Data = [6,7.5,8,0,1]
arr = np.array(Data)
arr


# In[6]:

Data1= [[1, 2, 3, 4], [5, 6, 7, 8]]
arr1 = np.array(Data1)
arr1


# arr1.shape

# In[16]:

arr1*arr1


# In[8]:

arr1.shape


# In[11]:

D =np.zeros(10)
D


# In[14]:

D1 = np.zeros((2,3))
D1


# In[15]:

D = np.arange(10)
D


# In[17]:

D[5]


# In[18]:

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr


# In[19]:

arr[2]


# In[20]:

arr[1,2]


# In[21]:

arr[:2]


# In[24]:

A =np.random.randn(3,2)
A


# In[25]:

A==.43344801


# In[27]:

D = arr[[4, 3, 0, 6]]
D


# In[31]:

arr = np.arange(16).reshape((4, 4))
arr


# In[40]:

arr.T


# In[41]:

arr.swapaxes(1, 2)


# In[ ]:

#pandas


# In[62]:

import pandas as pd
import numpy as np
obj = pd.Series([4, 7, -5, 3])
print(obj)


# In[63]:

obj2 =pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2


# In[66]:

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
frame


# In[96]:

data = {'state':['ohio','ohio','ohio','nevada','nevada'],'year':[2000,2001,2002,2001,2002], 'pop':[15,17,36,24,29]}
frame =pd.DataFrame(data)
frame


# In[97]:

D =pd.DataFrame(data, columns=['year','state','pop'])
D


# In[98]:

D1 =pd.DataFrame(data,columns=['year','state','pop','debt'], index=['one','two','three','four','five'])
D1


# In[99]:

D1['debt']=16.5
D1


# In[100]:

D1['debt'] =np.arange(5)
D1


# In[102]:

f = lambda x: x*x
D1['pop'].apply(f)


# In[81]:

D1.values


# In[82]:

D1.index


# In[86]:

D2 = D1.reindex(['a','b','c','d','e'])
D2


# In[92]:

D2.drop(['debt'],axis=1)


# In[94]:

D2.drop('b')


# In[104]:

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})
df3 = df1+df2
df3


# In[105]:

pd.merge(df1,df2)


# In[107]:

print(df1)


# In[109]:

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],'key2' : ['one', 'two', 'one', 'two', 'one'],'data1' : np.random.randn(5),
'data2' : np.random.randn(5)})
df


# In[110]:

grouped = df['data1'].groupby(df['key1'])
grouped


# In[111]:

grouped.sum()


# In[112]:

grouped.mean()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



