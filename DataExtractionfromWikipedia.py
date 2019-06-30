# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:02:34 2019

@author: S534629
"""

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