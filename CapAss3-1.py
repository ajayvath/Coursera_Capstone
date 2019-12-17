#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
#MyWeek3PD.csv
df1 = pd.read_csv('MyWeek3PD.csv')
df2 = pd.read_csv('Geospatial_Coordinates.csv')

df3 = pd.merge(left=df1, right=df2, left_on='Postcode', right_on='Postal Code')
df3.drop('Postal Code',axis=1, inplace=True)
df3


# In[ ]:




