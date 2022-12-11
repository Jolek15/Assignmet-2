#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def call_file(Electricity, sheet_name, countries):

    df_electric = pd.read_excel(Electricity, sheet_name, skiprows=3)
    df_electric = df_electric.drop(Cols, axis=1)
    df_electric = df_electric.drop('2021',axis = 1)
    df_electric = df_electric.set_index('Country Name')
    df_electric = df_electric.loc[countries, Years]
    
    return df_electric, df_electric.transpose()


# In[54]:


Electricity = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=excel')
Coal = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.COAL.ZS?downloadformat=excel')
Nuclear = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.NUCL.ZS?downloadformat=excel')
Petrol = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.PETR.ZS?downloadformat=excel')
Transmission = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.LOSS.ZS?downloadformat=excel')




sheet_name = ('Data')
Cols = ['Country Code','Indicator Name','Indicator Code']
countries = ["Australia","Brazil","Colombia","France","Japan","Mexico","Senegal","United Kingdom"]
Years = ['2008','2009','2010','2011','2012','2013','2014']

df_electric, df_electric_transpose = call_file(Electricity, sheet_name,countries)
df_coal, df_coal_transpose = call_file(Coal, sheet_name,countries)
df_nuclear, df_nuclear_transpose = call_file(Nuclear, sheet_name,countries)
df_petrol, df_petrol_transpose = call_file(Petrol, sheet_name,countries)
df_transmission, df_transmission_transpose = call_file(Transmission, sheet_name,countries)


# In[55]:


df_electric


# In[56]:


df_electric_transpose


# In[57]:


df_coal


# In[58]:


df_coal_transpose


# In[59]:


df_petrol


# In[60]:


df_petrol_transpose


# In[92]:


df_nuclear


# In[95]:


df_nuclear_transpose


# In[61]:


df_transmission


# In[62]:


df_transmission_transpose


# In[63]:


def plt_plot(year, prod, title, label, color, xaxes, yaxes):
    
    plt.figure(figsize=(10,6))
    
    for i in range(len(prod)):
        plt.plot(year, prod[i], label=label[i], color=color[i])
    plt.title(title)
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.legend(bbox_to_anchor=(1,1.01))
    plt.show()
    
    return


# In[64]:


prod = [df_coal_transpose['Australia'],df_coal_transpose['Brazil'],df_coal_transpose['Colombia'],
     df_coal_transpose['France'],df_coal_transpose['Japan'],df_coal_transpose['Mexico'],
     df_coal_transpose['Senegal'],df_coal_transpose['United Kingdom']]
year = df_coal_transpose.index
title = "Electricity production from Coal Sources for each Country"
label = ["AUS", "BRA", "COL", "FRA", "JPN", "MEX", "SEN", "GBR"]
color = ['magenta','blue','green','yellow', 'black', 'purple', 'brown', 'red']
xaxes = "Years"
yaxes = "Coal electricity production rate"

plt_plot(year, prod, title, label, color, xaxes, yaxes)


# In[65]:


coal = df_coal_transpose.iloc[:4, :]
nuclear = df_nuclear_transpose.iloc[:4, :]
petrol = df_petrol_transpose.iloc[:4, :]


# In[66]:


plt.figure()
df_electric.plot(kind='bar',stacked=False,
    title='Access to Electricity of each country',
    width=0.5, figsize = (10,10))
plt.xlabel('Country Name')
plt.ylabel('Access to electricity rate')
plt.legend(bbox_to_anchor=(1,1.01))
plt.show()


# In[67]:


df_transmission.plot(kind='bar',stacked=False,
    title='Electricity transmission loss rate of each country', figsize = (10,12))
plt.xlabel('Countries')
plt.ylabel('Electricity transmission loss rate')


# In[68]:


def bar_chart_subplot(years,petrol, labels):
    x = len(petrol)
    plt.figure(figsize=(22,8))
    for i in range(x):
        plt.subplot(2,4,i+1).set_title(labels[i],fontsize=15)
        plt.tight_layout()
        plt.bar(years,petrol[i])   
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=16,rotation=90)
    plt.show()
    
    
    
   


# In[69]:



years = df_petrol_transpose.index
petrol = [df_petrol_transpose['Australia'],df_petrol_transpose['Brazil'],df_petrol_transpose['Colombia'],
    df_petrol_transpose['France'],df_petrol_transpose['Japan'],df_petrol_transpose['Mexico'],
    df_petrol_transpose['Senegal'],df_petrol_transpose['United Kingdom']]
labels = ["Australia petrol production rate", "Brazil petrol production rate", "Colombia petrol production rate", "France petrol production rate", "Japan petrol production rate", "Mexico petrol production rate", "Senegal petrol production rate", "United Kingdom petrol production rate"]
bar_chart_subplot(years, petrol, labels)


# In[ ]:





# In[96]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




