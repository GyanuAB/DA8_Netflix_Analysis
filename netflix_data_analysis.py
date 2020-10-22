#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


N_data = pd.read_csv("Netflix_data.csv")


# In[5]:


N_data


# In[6]:


N_data.T


# In[48]:


N_data.isnull().sum()


# In[10]:


def data_inv(N_data):
    print('netflix movies and shows: ',N_data.shape[0])
    print('dataset variables: ',N_data.shape[1])
    print('-'*10)
    print('dateset columns: \n')
    print(N_data.columns)
    print('-'*10)
    print('data-type of each column: \n')
    print(N_data.dtypes)
    print('-'*10)
    print('missing rows in each column: \n')
    c=N_data.isnull().sum()
    print(c[c>0])
data_inv(N_data)


# In[22]:


print('In all, there are   :',N_data['rating'].nunique(),'types of ratings in the dataset: ',N_data['rating'].unique())


# In[ ]:


## Above is all types of rating that is present in dataset.


# In[53]:


print('In all, there are  :\n',
      N_data['release_year'].nunique(),'years in the dataset: \n',N_data['release_year'].unique())


# In[40]:


sns.countplot(x="type", data=N_data,)


# In[ ]:


##  AS we can see the number of movies is more than the Tv shows in netflix.


# In[11]:


for i in N_data.index:
    if N_data.loc[i,'rating']=='UR':
        N_data.loc[i,'rating']='NR'


# In[12]:


plt.figure(figsize=(8,6))
N_data['rating'].value_counts(normalize=True).plot.bar()
plt.title('Distribution of rating categories')
plt.xlabel('rating')
plt.ylabel('relative frequency')
plt.show()


# In[ ]:


# Above is the graph for the visualization of the distribution of the ratings.


# In[13]:


plt.figure(figsize=(10,8))
sns.countplot(x='rating',hue='type',data=N_data)
plt.title('comparing frequency between type and rating')
plt.show()


# In[ ]:


# Difference in between the Frequency of TV shows and Movies having same rating.


# In[14]:


N_data['country'].value_counts().sort_values(ascending=False)


# In[ ]:


# Countries haing contribution in the netflix market.


# In[15]:


top_productive_countries=N_data[(N_data['country']=='United States')|(N_data['country']=='India')|(N_data['country']=='United Kingdom')|(N_data['country']=='Japan')|
                             (N_data['country']=='Canada')|(N_data['country']=='Spain')]
plt.figure(figsize=(10,8))
sns.countplot(x='country',hue='type',data=top_productive_countries)
plt.title('comparing between the types that the top countries produce')
plt.show()


# In[ ]:


# Visualization of contribution that are given by different countries in the number of movies and TV shows in netflix market.


# In[34]:


print("The Year-wise distribution of Netflix shows")
year_no_of_shows=N_data["release_year"].value_counts().sort_values(ascending=False)
plt.figure(figsize=(20,10))
year_no_of_shows.plot(title='Years with the number of Netlfix Shows',kind="bar")


# In[35]:


plt.figure(figsize=(12,12))
N_data.rating.value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title('Number of appearances in dataset')
plt.show()


# In[ ]:


# The above pie graph shows percentage of the total rating of movies and shows in netflix data.


# In[ ]:


# So this is all about netflix data analysis for now . But i will continue workon on it when i will get time.


#  Akhil Bhall

