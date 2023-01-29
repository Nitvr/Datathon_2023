#!/usr/bin/env python
# coding: utf-8

# In[75]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# In[103]:


df = pd.read_csv("./sc-est2019-agesex-civ.csv")
new_df = df.iloc[:,3:]#select the relevant columns
new_df


# In[122]:


#Test if we can use AR model to estimate the population in 2020
test_change_rate = []
for year in range(4,14):
    diff = new_df.iat[1,year+1]-new_df.iat[0,year]
    diff_rate = diff/new_df.iat[0,year]
    test_change_rate.append(diff_rate)#acquire a list of all the change rates
    

test_change_rate
test_change_rate2 = test_change_rate[1:]

print(pearsonr(test_change_rate[0:-1],test_change_rate2))#correlation coefficient

#since the correlation coefficient is around 0.7, it proves that AR model is suitable for our estimation


# In[123]:


test_change_rate


# In[49]:


year_lst = []
for years in range(2010,2020):
    year_lst.append(years)
year_lst


# In[59]:


plt.scatter(year_lst,test_change_rate,color='b',label='Mortality Rate Data')

plt.legend(loc=2)
plt.xlabel('Year')
plt.ylabel('Change_Rate')
#plt.show()


# In[124]:


from statsmodels.tsa.ar_model import AutoReg
def ar_estimate(change_rate):
    p = 1#we make our prediction based on change rate of last 10 years
    model_fit = AutoReg(change_rate,lags = p).fit()
    params = model_fit.params
    return model_fit.predict(start = len(change_rate),end = len(change_rate))


# In[128]:


population_lst = []
for row in range(len(df)-1):#it would loop out of range without "-1"
    change_rate = []
    for year in range(4,14):
        diff = new_df.iat[row+1,year+1]-new_df.iat[row,year]
        diff_rate = diff/new_df.iat[row,year]
        change_rate.append(diff_rate)#acquire a list of all the change rates
    rate_2020 = ar_estimate(change_rate)#Use AR model to calculate the change rate for 2020
    population = new_df.iat[row,-1] * (1 + rate_2020)#calculate the population in 2020 for that particular row
    population_lst.append(float(population))
   # print(type(int(population)))

            
    


# In[138]:


final_df = df.iloc[:-1,3:7]
final_df["2020_Population"] = population_lst

final_df.to_csv("2020_population_prediction.csv")


# In[ ]:




