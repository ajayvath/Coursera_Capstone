#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_csv('MyWeek3PD.csv')
df.head()


# In[14]:


df_clean = df[(df != 'Not assigned').all(1)]
df_clean.head(5)


# In[30]:


df_clean['Neighbourhood'] = df['Neighbourhood'].astype(str)
result_df = df_clean.groupby(['Postcode','Borough'], sort=False).agg( ','.join)
result_df


# In[26]:


result_df


# In[45]:


type(result_df)
result_df.shape


# In[ ]:




