
# coding: utf-8

# In[90]:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
get_ipython().magic('matplotlib inline')



# In[91]:

DF = pd.read_csv("C:/Users/as/Desktop/DATA SETs/flipkart_com-ecommerce_sample.csv",na_values=["No rating available"])
DF.head()


# In[92]:

DF.info()


# In[93]:

#list=['crawl_timestamp','product_url','image','description','product_specifications']
#DF=DF.drop(list,axis=1)


# In[94]:

DF.head()


# In[ ]:




# In[ ]:




# In[95]:

DF["discount_per"] = ((DF.retail_price - DF.discounted_price)*100)/DF.retail_price
DF.discount_per.head()


# In[96]:

def category(DF, level=1):
    if level == 1:
       category = (DF.product_category_tree.apply(lambda x: re.split(" >> ", x)[0])[2:] )
    else :
       category = DF.product_category_tree.apply(lambda x: re.split(" >> ", x)[level:(level+1)])
    return category


# In[97]:

print(category(DF, level=4))


# In[98]:

#print(DF['product_category_tree'])
DF["primary_category"] = category(DF, level=1)
DF["secondary_category"] = category(DF, level=2)



# In[99]:

print(DF.primary_category.head(5), "\n\n")
print(DF.secondary_category.head(5))


# In[100]:

print("Missing value percentage", "\n\nProduct rating: ", round(DF.product_rating.isnull().sum()*100/DF.shape[0], 2), "%",
      "\nOverall rating: ", round(DF.overall_rating.isnull().sum()*100/DF.shape[0], 2), "%")


# In[101]:

groupby_df = pd.DataFrame(DF.groupby("primary_category").agg({
    "discount_per": [np.mean],
    "primary_category": ["count"]
}))

groupby_df.columns = ["_".join(col) for col in groupby_df.columns]
groupby_df = groupby_df.sort_values(by = ["primary_category_count"], ascending=False)
groupby_df = groupby_df[groupby_df.primary_category_count > 80]



# In[102]:

groupby_df


# In[103]:

groupby_df.reset_index(inplace=True)


# In[104]:

print(groupby_df.head())
print(groupby_df.info())
print(groupby_df.describe())


# In[105]:


sns.barplot(data=groupby_df.sort_values(["primary_category_count"], ascending=False),
            y="primary_category", x = "primary_category_count")
plt.xlabel("Number of products")
plt.ylabel("Product Category")



# In[ ]:




# In[ ]:




# In[ ]:




