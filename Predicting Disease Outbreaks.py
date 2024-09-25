#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt


# In[14]:


country_wise_latest = pd.read_csv('country_wise_latest.csv')
covid_19_clean_complete = pd.read_csv('covid_19_clean_complete.csv')
day_wise = pd.read_csv('day_wise.csv')
full_grouped = pd.read_csv('full_grouped.csv')
usa_county_wise = pd.read_csv('usa_county_wise.csv')
worldometer_data = pd.read_csv('worldometer_data.csv')

{
    "country_wise_latest": country_wise_latest.head(),
    "covid_19_clean_complete": covid_19_clean_complete.head(),
    "day_wise": day_wise.head(),
    "full_grouped": full_grouped.head(),
    "usa_county_wise": usa_county_wise.head(),
    "worldometer_data": worldometer_data.head(),
}


# In[16]:


#Top ten countries with the most confirmed cases
top_10_countries = country_wise_latest[['Country/Region', 'Confirmed']].sort_values(by='Confirmed', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_10_countries['Country/Region'], top_10_countries['Confirmed'], color='skyblue')
plt.xlabel('Confirmed Cases')
plt.title('Top 10 Countries with Most Confirmed COVID-19 Cases')
plt.gca().invert_yaxis()
plt.show()


# In[17]:


#Calculates death rates
country_wise_latest['Death Rate (%)'] = (country_wise_latest['Deaths'] / country_wise_latest['Confirmed']) * 100

#Shows the top ten countries with the highest death rates
top_10_death_rates = country_wise_latest[['Country/Region', 'Death Rate (%)']].sort_values(by='Death Rate (%)', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_10_death_rates['Country/Region'], top_10_death_rates['Death Rate (%)'], color='salmon')
plt.xlabel('Death Rate (%)')
plt.title('Top 10 Countries with Highest COVID-19 Death Rates')
plt.gca().invert_yaxis()
plt.show()


# In[ ]:




