
# coding: utf-8

# In[5]:

import pandas as pd
obj =pd.Series([4, 7, -5, 3],['a','b','c','d'])
print(obj)


# In[7]:

obj['a']


# In[14]:

s = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
print(pd.series(s))


# In[16]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}
pd.Series(d)


# In[19]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[20]:

pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])


# In[26]:

import numpy as np
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)


# In[28]:

'f' in s


# In[29]:

'a' in s


# In[32]:

s.get('f' , np.nan)


# In[33]:

s+s


# In[35]:

s*4


# In[36]:

s[1:] + s[:-1]


# In[39]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df=pd.DataFrame(d)
print(df)


# In[40]:

pd.DataFrame(d, index=['b' , 'c', 'd'],columns=['two', 'three'])


# In[41]:

df.index


# In[42]:

df.columns


# In[44]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'), (2,3.,"World")]
pd.DataFrame(data)


# In[45]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
 


# In[55]:

print(pd.DataFrame(data).values)


# In[57]:

df['one']


# In[58]:

df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
print(df)


# In[68]:

del df['two']
print(df)


# In[69]:

df['Foo']= 'bar'
print(df)


# In[70]:

df['Too']= df['one'][:2]
print(df)


# In[75]:

df.reindex(['d', 'a', 'b','c'])
print(df)


# In[85]:

df4 =del df(['flag' ,'Foo'])
print(df4)
df4.reindex(range(6), method= 'ffill')


# In[88]:

df.drop('b')
print(df)


# In[90]:

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
 columns=['one', 'two', 'three', 'four'])
print(data)


# In[92]:

F =data.ix[['Colorado', 'Utah'], [3, 0, 1]]
print(F)


# In[94]:

arr = np.arange(12). reshape(3,4)
print(arr)


# In[95]:

arr[0]


# In[97]:

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print (frame)


# In[99]:

obj =pd. Series(range(4), index=['d', 'a', 'b', 'c'])
f = obj.sort_index
print(f)


# In[102]:

obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
g  = obj.order()
print(g)


# In[103]:

df5 = pd.read_csv('D:/sarita/input.csv ')
print(df5)


# In[106]:

df5['a']


# In[111]:

df5[['a' , 'b','d']][1:3]


# In[112]:

df5[['c', 'd', 'message']][1:2]


# In[1]:

df6 = df5.reindex('message','hell')
print(df6)                  


# In[ ]:




# df5.set_index('message')

# In[124]:

df7 = pd.read_csv('D:/sarita/input.csv')
print(df7)


# In[127]:

pd.isnull (df7)


# In[128]:

df7.dropna()


# In[129]:

df7.fillna('love')


# In[131]:

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1':range(7)})
df1


# In[133]:

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2':range(3)})
df2


# In[134]:

G = pd.merge(df1, df2)
print(G)    


# In[136]:

D = np.arange(12).reshape((3,4))
print(D)


# In[137]:

D1 = np.concatenate([D,D],axis = 1)
print(D1)


# In[144]:

df =pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'], 'key2' : ['one', 'two', 'one', 'two', 'one'], 'data1' : np.random.randn(5), 'data2' : np.random.randn(5)})
print(df)


# In[146]:

grouped = df['data1'].groupby(df['key1'])
print(grouped)


# In[147]:

grouped.mean()


# In[148]:

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means)


# In[149]:

means.unstack()


# In[153]:

Means = df.groupby(['key1', 'key2'])[['data2']].mean()
print(Means)


# In[158]:

s_grouped = df.groupby(['key1', 'key2'])['data2']
print(s_grouped)


# In[159]:

s_grouped.mean()


# In[163]:

import pandas as pd

dir(pd)


# In[ ]:



