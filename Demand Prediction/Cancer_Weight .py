#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
from scipy.special import logsumexp


# In[5]:


np.seterr(divide = 'ignore') 


# In[33]:


w_age = 0.2313767524360226 
w_sex = 0.7686232475639774


# In[6]:


df = pd.read_csv('2010-2019 Breast Cancer Incidence (With Crude Rates).txt', delimiter="\t")
df.to_csv('cancer(with crude rates).csv', index = False)
df['Age'] = df['Age Groups'].str[0:2]
df = df.groupby(['Year', 'Age', 'Sex Code'],as_index=False).agg({'Crude Rate': 'sum'})


# In[8]:


#Standardize Crude Rate 
num_rows = df.shape[0]
min_val = df['Crude Rate'].min()
diff = df['Crude Rate'].max()-df['Crude Rate'].min()
def get_standardized_data (rate):
    return (rate - min_val)/diff

df['S Rate']=df['Crude Rate'].apply(get_standardized_data)
df


# In[63]:


data = df.groupby(['Sex Code', 'Age'],as_index=False).agg({'S Rate': 'mean'})
data.to_csv("data.csv")


# In[44]:


data = df.groupby(['Sex Code', 'Age', 'Year'],as_index=False).agg({'S Rate': 'sum'})
data_F_20 = data[data['Sex Code']=='F']
data_F_20 = data[data['Age']=='20']
num_rows = data_F_20.shape[0]
data_F_20


# In[58]:


stan_rate = np.array(data_F_20['S Rate'])
max_rate = stan_rate.max()
min_rate = stan_rate.min()
ave_rate = (max_rate + min_rate)/2
sum_rate = stan_rate.sum()
p_values = []

sum_plus = 0
for i in range (num_rows):
    sum_plus += (max_rate - stan_rate[i])**2
dis_plus = np.sqrt(w_age * sum_plus)

sum_minus = 0
for i in range (num_rows):
    sum_minus += (min_rate - stan_rate[i])**2
dis_minus = np.sqrt(w_sex * sum_minus)

w_F_20 = dis_minus/(dis_plus+dis_minus)
print (w_F_20)

