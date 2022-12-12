#!/usr/bin/env python
# coding: utf-8

#I import needed libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def call_file(Electricity, sheet_name, countries):
    
    """
    A function that reads in excel file in the world bank format and returns 
    the original and transposed format. 
    Args:
    electricity (str): name of the dataframe
    sheet name: name of the excel sheet 
    countries: a list of countries needed for our visualization
    returns:
    df_electric, df_electric_transpose: A tuple containing the worldbank data
    and the transpose.
    """
# read files into dataframe using pandas 
    df_electric = pd.read_excel(Electricity, sheet_name, skiprows=3)
#drop irrelevant columns to re-process our data
    df_electric = df_electric.drop(Cols, axis=1)
    df_electric = df_electric.drop('2021',axis = 1)
#extract the needed rows and columns  
    df_electric = df_electric.set_index('Country Name')
    df_electric = df_electric.loc[countries, Years]
#returns our needed dataframe with the transpose
    return df_electric, df_electric.transpose()

#Declaring values for our function
#inputing the world bank files with different indicators
Electricity = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=excel')
Coal = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.COAL.ZS?downloadformat=excel')
Nuclear = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.NUCL.ZS?downloadformat=excel')
Petrol = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.PETR.ZS?downloadformat=excel')
Transmission = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.LOSS.ZS?downloadformat=excel')

#stating our sheet name
sheet_name = ('Data')
#declaring our data columns
Cols = ['Country Code','Indicator Name','Indicator Code']
#declaring the needed countries
countries = ["Australia","Brazil","Colombia","France","Japan","Mexico","Senegal","United Kingdom"]
#declaring the needed years in a list
Years = ['2008','2009','2010','2011','2012','2013','2014']

#assigning our variables to our function
df_electric, df_electric_transpose = call_file(Electricity, sheet_name,countries)
df_coal, df_coal_transpose = call_file(Coal, sheet_name,countries)
df_nuclear, df_nuclear_transpose = call_file(Nuclear, sheet_name,countries)
df_petrol, df_petrol_transpose = call_file(Petrol, sheet_name,countries)
df_transmission, df_transmission_transpose = call_file(Transmission, sheet_name,countries)

#Reading our dataframes and their transposes for used indicators
#(Indicators: access to electricity,electricity transmission and distribution loss, electricity production from coal, nuclear and petroleum for the selected countries)

print(df_electric)
print(df_electric_transpose)

print(df_coal)
print(df_coal_transpose)

print(df_petrol)
print(df_petrol_transpose)

print(df_nuclear)
print(df_nuclear_transpose)

print(df_transmission)
print(df_transmission_transpose)

#Define a function called plt_plot to show the electricity production from coal sources for each country from 2008 to 2014
def plt_plot(year, prod, title, label, color, xaxes, yaxes):
    ''' A function that produces a line plot to show the electricity production from coal sources of each countries from 2008 to 2014
    year: years ranging from 2008 - 2014
    prod: production from coal sources of each country
    title: Electricity production from Coal Sources for each Country  
    labels:
        xlabel: Years, ylabels: coal electricity production rate.
    color: color of line plots
    '''
    plt.figure(figsize=(10,6))
    #loop over the columns
    for i in range(len(prod)):
        plt.plot(year, prod[i], label=label[i], color=color[i])
    plt.title(title, fontsize=10)
    plt.xlabel(xaxes, fontsize=12)
    plt.ylabel(yaxes, fontsize=10)
    plt.legend(bbox_to_anchor=(1,1.01))
    plt.savefig('Lineplot.png')
    plt.show()
    return

#declaring values for the function
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

#A bar plot showing the access to electricity of each country from 2008 t0 2014
plt.figure()
df_electric.plot(kind='bar',stacked=False,
    width=0.8, figsize = (25,14))
''' A function that produces a bar plot to show the access to electricity of each country from 2008 to 2014
year: years ranging from 2008 - 2014
title: Access to Electricity of each country
labels:
    xlabel: Country name, ylabel: Access to electricity rate.
'''
plt.title('Access to Electricity of each country',fontsize=35)
plt.xlabel('Country Name',fontsize=25)
plt.ylabel('Access to electricity rate',fontsize=28)
plt.legend(bbox_to_anchor=(1,1.01), fontsize=22)
plt.yticks(fontsize=20)
plt.xticks(fontsize=22)
plt.savefig('Access Bar plot.png')
plt.show()

#A bar plot showing electricity transmission and distribution loss rate for each country
df_transmission.plot(kind='bar',stacked=False,
     width=0.8, figsize = (24,15))
''' A function that produces a bar plot to show electricity transmission loss rate of each country from 2008 to 2014
year: years ranging from 2008 - 2014
title: Electricity transmission loss rate of each country
labels:
    xaxes: Country name, yaxes: electricity transmission loss rate.
'''
plt.title('Electricity transmission loss rate of each country',fontsize=40)
plt.xlabel('Country name',fontsize=35)
plt.ylabel('Electricity transmission loss rate', fontsize=30)
plt.yticks(fontsize=28)
plt.xticks(fontsize=35)
plt.legend(fontsize=24)
plt.savefig('Elec Bar plot.png', dpi=300)
plt.show()
#A function called bar_chart_subplot using subplots to show electricity petroleum production rate of each country from 2008 to 2014
def bar_chart_subplot(years,petrol, labels):
    ''' A function that produces a bar subplot to show the electricity production from petroleum sources of each country from 2008 to 2014
    year: years ranging from 2008 - 2014
    petrol: production from petroleum sources of each country
    
    labels:
        xlabel: Years, ylabels: petrol electricity production rate.
    color: color of line plots
    '''
    x = len(petrol)
    plt.figure(figsize=(22,8))
    for i in range(x):
        plt.subplot(2,4,i+1).set_title(labels[i],fontsize=15)
        plt.tight_layout()
        plt.bar(years,petrol[i])   
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=16,rotation=90)
    plt.show()
    
    
#Declaring values for the function    
years = df_petrol_transpose.index
petrol = [df_petrol_transpose['Australia'],df_petrol_transpose['Brazil'],df_petrol_transpose['Colombia'],
     df_petrol_transpose['France'],df_petrol_transpose['Japan'],df_petrol_transpose['Mexico'],
     df_petrol_transpose['Senegal'],df_petrol_transpose['United Kingdom']]
labels = ["Australia petrol production rate", "Brazil petrol production rate", "Colombia petrol production rate", "France petrol production rate", "Japan petrol production rate", "Mexico petrol production rate", "Senegal petrol production rate", "United Kingdom petrol production rate"]
bar_chart_subplot(years, petrol, labels)

#Creating a dataframe that contains Japan Eletricity production from Coal, Petroleum, Nuclear data and their transmission/distribution loss data.
japan = pd.DataFrame(
{'Coal Production': df_coal_transpose['Japan'],
'Petrol Production': df_petrol_transpose['Japan'],
'Transmission loss': df_transmission_transpose['Japan'],
'Nuclear Production': df_nuclear_transpose['Japan']},
['2008','2009','2010','2011','2012','2013','2014'])

#Using numpy to show the correlation between Japan Electricity production from coal and nuclear sources
corr = np.corrcoef(japan['Coal Production'], japan['Nuclear Production'])

print(corr)
#A correlation between Japan electricity production from coal, petroleum, nuclear sources and their transmission loss from 2008 to 2014.
japan.corr()

#Using Seaborn to plot a heat map of Japan's electricity production from coal, petroleum, nuclear sources and their transmission loss from 2008 to 2014.
def corr_heatmap(data, title):
    """A function that produces a correlation heatmap for japan's 

    This function calculates the correlation between the columns in the
    given data and plots a heatmap of the correlations.

    Args:
        data: A dataframe containing the data to plot.
        title: The title to use for the plot.
    """
    corr = data.corr()
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
    
    plt.title('Japan Correlation heatmap')
    plt.figure(figsize=(8,8))
    plt.savefig('Heatmap.png')
    plt.show()

corr_heatmap(japan, title)





