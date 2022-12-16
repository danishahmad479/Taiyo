#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas 
import requests
from bs4 import BeautifulSoup


# In[2]:


session = requests.Session()
url = "https://opentender.eu/start"
soup = BeautifulSoup(session.get(url).text, "html.parser")
# print(soup)


# In[3]:


Bname = []
Btender = []
Bvolume = []
link = soup.findAll("li",class_="portal-link")
for i in link:
    links = f'https://opentender.eu{i.a["href"]}'
#     print(links)
    data2 = session.get(links)
    soup2 = BeautifulSoup(data2.text,"html.parser")
#     print(soup2)
    sub_link =  soup2.findAll('p',class_="card-content-subhead")
#     print(sub_link)
    for j in sub_link[0:1]:
        Sub_link = f"https://opentender.eu{j.find_next('a')['href']}"
#         print(Sub_link)
        data3 =  session.get(Sub_link)
        soup3 =  BeautifulSoup(data3.text,"html.parser")
#         print(soup3)
        name = soup3.find_all('table',class_="tables")
        for k in range(len(name)):
            try:
                Name = name[k].text
            except:
                Name = " "

            print(Name)
#             try:
#                 tender = name[k].find_next('tbody').find_next('tr').find_next('tr').find_next('td').find_next('td').find_next('td').find_next('td').text
#             except:
#                 tender = " "
#             print(tender)
#             try:
#                 volume = name[k].find_next('tbody').find_next('tr').find_next('tr').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text
#             except:
#                 volume = " "
#             print(volume)
            
        Bname.append(Name)
#         Btender.append(tender)
#         Bvolume.append(volume)

            

  


# In[4]:


Data  = pandas.DataFrame({"All_info" :Bname })


# In[5]:


Data


# In[8]:


Data.to_csv(r"D:\Taiyo\Taiyo.csv",index= False)


# In[ ]:




