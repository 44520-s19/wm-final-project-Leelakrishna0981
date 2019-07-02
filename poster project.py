# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:02:34 2019

@author: S534629
"""
#below code is to store wikipedia data into csv file
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL="https://en.wikipedia.org/wiki/List_of_largest_pharmaceutical_companies_by_revenue"
response=requests.get(URL)
soup=BeautifulSoup(response.text, 'html.parser')

table= soup.find('table',{'class':'sortable wikitable'}).tbody

rows=table.find_all('tr')

columns=[v.text.replace('\n','') for v in rows[0].find_all('th')]

df= pd.DataFrame(columns=columns)

for i in range(1, len(rows)):
    tds=rows[i].find_all('td')
    
    if len(tds)==4:
        values=[tds[0].text,tds[1].text.replace('\n','').replace('\xa0',''),'',
                tds[2].text.replace('\n','').replace('\xa0',''),'','','','','','','','']
    else:
        values=[td.text.replace('\n','').replace('\xa0','') for td in tds]
    
    
    df=df.append(pd.Series(values, index=columns), ignore_index=True)
    
    df.to_csv(r'C:\Users\S534629\Downloads\Web mining\Assignments\Project'+
              'pharmatop10.csv',index=False)
    
# Plotting the graph with the help of above obtained data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def readcsv(filename):
    data = pd.read_csv(filename) 
    return(np.array(data))

data1=readcsv('ProjectpharmaTop10.csv')

#storing different companies yearwise revenues from the csv table
JNJ=[data1[0][4],data1[0][5],data1[0][6]]
Roche=[data1[1][4],data1[1][5],data1[1][6]]
pfizer=[data1[2][4],data1[2][5],data1[2][6]]
Novartis=[data1[3][4],data1[3][5],data1[3][6]]
Bayer=[data1[4][4],data1[4][5],data1[4][6]]

#storing years of revenue
years=['2016','2017','2018']

#plotting a line graph
plt.plot(years,JNJ[::-1],'b.-',label='JNJ',marker="s")
plt.plot(years,Roche[::-1],'r.-',label='Roche',marker="P")
plt.plot(years,pfizer[::-1],'m.-',label='pfizer',marker="d")
plt.plot(years,Novartis[::-1],'y.-',label='Novartis',marker="o")
plt.plot(years,Bayer[::-1],'c.-',label='Bayer',marker="*")

plt.title('Pharma Company and their Revenue in last 3 years',fontweight='bold')
plt.ylabel('Revenue in USD billions',fontweight='bold')
plt.xlabel('Years',fontweight='bold')
plt.ylim(0,90)
plt.legend()
plt.savefig('pharma_graph.png',transparent='True')
