# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:21:59 2018

@author: Xinyue
"""

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import os
os.chdir('C:\\Users\\HP\\Documents\\研二上哥大课件\\15 Tools for Analytics\\小组项目')

data=[]

# # 从Amazon的商品名进入EBay搜索结果页
title = 'Toshiba 43LF621U19 43-inch 4K Ultra HD Smart LED TV HDR - Fire TV Edition'
stitle = title.replace(' ','+')
url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + stitle

response = requests.get(url) 
if response.status_code == 200:
    print("Success")
    results_page = BeautifulSoup(response.content,'lxml')
else:
    print("Failure")
#print(results_page.prettify())


# # 在搜索页中找到第一个商品的关键信息并记录link,name,price,rate,num
products_list = results_page.find_all('li',class_ = 's-item')[0]

link = products_list.find('a').get('href')
name = products_list.find('h3').text
price = products_list.find('div',class_='s-item__detail s-item__detail--primary').text
rate = products_list.find('div',class_='b-starrating').text[:3]
num_text=products_list.find('span',class_='s-item__reviews-count').text
num = re.search(r'(\d)+',num_text).group(1)

data.append([link,name,price,rate,num])

# # 每次12*5存储进一张特别命名的csv表格
timename = time.strftime("%Y%m%d_%H", time.localtime()) 
with open('Ebay_'+timename+'.csv','w') as fp:
    writer=csv.writer(fp)
    writer.writerows(data)


with open('Ebay_'+timename+'.csv','r') as fp:
    r=csv.reader(fp)
    d=list(r)






