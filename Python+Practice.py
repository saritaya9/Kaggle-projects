
# coding: utf-8

# In[1]:

x = 5 + 4

print(x)


# In[3]:

print ('hello,world!')


# In[4]:

x =4
print(x*x)


# In[7]:

x = 'hello'
print(x*2)


# In[9]:

a,b = 1,2
a,b = b,a
print(a)
a+b


# In[11]:

a,b = 2,6
a,b = b,a+2
print(a,b)


# In[14]:

x = ''' this is 
multiline string
the'''
print (x)


# In[17]:

def square(x):
    return x*x
square(2)+ square(3)


# In[18]:

square(square(3))


# In[19]:

x,y = 0,0
def  incr(x):
    y = x+1
    return y
incr(5)
print(x,y)


# In[22]:

numcalls =0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x  * x
print (square(5))


# In[26]:

x = 1
def f():
    return x
print (x)
print (f())


# In[104]:

x = 1

def f():
    #x = 2
    y = x
    #x = 2
    return x + y
print(x)
print(f())
print(x)


# In[37]:

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x,y)


# In[103]:

def fxy(f, x, y):
      return f(x)+f(y)



cube = lambda  x: x ** 3
fxy (cube, 2, 3)


# In[47]:


istrcmp('LaTeX', 'Latex')


# In[48]:

x = 2
y = 4
x>y


# In[49]:

x = 42
if x < 10:
    print("one digit number")
elif x < 100:
    print(" two digit number")
    
else:
    print("no")


# In[95]:

python add.py


# In[100]:

List = [1, 2, range(3)]
print(List)
x = range(10)

L1 = [r for r in range(10)]

print(L1)


# In[71]:

a = [ 1,2, 3]
b = [4,5,6]
c = a+b
print (c)
a[0:2]
a[:2]
a.append(9)
print(a)


# In[74]:

a =  [3, 4, 9, 8]
a.sort()
print(a)


# In[78]:

x = {9, 8, 4, 5}
x.add(7)
print(x)


# In[84]:

x = ("askgfjbvbn")
x.split(',')
print(x)


# In[94]:

def wordcount(filename):
    return len(open(filename).read().split())


# In[91]:

def square(x):
    return x  * x
map(square,range(5))


# In[93]:

import numpy as np
np.square(3)


# In[108]:

f1 = open ('D://sarita.txt','w')
f1.write('fdlklklfdklkllklklklklklklkkllklklklklklklk')
f1.close()


# In[114]:

f = int(input('Enter a number behenchod'))
r = f*f
print(r)


# In[155]:

string="Monty Python ! And the holy Grail ! \n"
word_freq={}
for tok in string.split():
    if tok in word_freq:
        word_freq [tok]+=1
    else:   
        word_freq [tok]=1
print(word_freq)        


# In[158]:

import csv
f=open('D://sarita.txt')
f1= csv.reader(f)
print(f1)


# In[128]:

inputstring = 'This is an example of eating. The sentence splitting willsplit on sent markers. Ohh really !!'
from nltk.tokenize import sent_tokenize
f = sent_tokenize(inputstring)
print(f)


# In[133]:

from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem(inputstring)
    


# In[161]:

from nltk import WordNetLemmatizer
wlem = WordNetLemmatizer()
wlem.lemmatize("playing")


# In[162]:

from nltk.corpus import stopwords


# In[137]:

from nltk.metrics import edit_distance
edit_distance("rain","shine")


# In[140]:

import nltk
from nltk import word_tokenize
s = "I was watching TV"
print (nltk.pos_tag(word_tokenize(s)))


# In[143]:

import nltk
from nltk import ne_chunk
f = "Mark is studying at Stanford University in California"
print(ne_chunk(nltk.pos_tag(word_tokenize(f)), binary=False))


# In[149]:

import nltk
from nltk.chunk.regexp import *
reg_parser = regexpParser('''
NP: {<DT>? <JJ>* <NN>*} # NP
P: {<IN>} # Preposition
V: {<V.*>} # Verb
PP: {<P> <NP>} # PP -> P NP
VP: {<V> <NP|PP>*} # VP -> V (NP|PP)*
''')

f="Mr. Obama played a big role in the Health insurance bill"
f_pos = nltk.pos_tag(nltk.word_tokenize(f))
f1=reg_parser.parse(f_pos)
print(f1)


# In[154]:

f =open("D://nyt.txt")
news_content=f.read()
print(news_content)


import nltk

s1 = nltk.sent_tokenize(news_content)

print(s1)

for sent_no,sentence in enumerate(nltk.sent_tokenize(news_content)):
    no_of_tokens=len(nltk.word_tokenize(sentence))
    print(no_of_tokens)


# In[152]:

# pos tagging
tagged=nltk.pos_tag(nltk.word_tokenize(sentence))
print(tagged)


# In[ ]:



