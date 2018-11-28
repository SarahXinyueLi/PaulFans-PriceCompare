# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:21:59 2018

@author: Xinyue
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import os
os.chdir('C:\\Users\\HP\\Documents\\研二上哥大课件\\15 Tools for Analytics\\小组项目')

titlelist=['Toshiba 43LF621U19 43-inch 4K Ultra HD Smart LED TV HDR - Fire TV Edition',\
           'Samsung Electronics UN32M4500A 32-Inch 720p Smart LED TV (2017 Model)',\
           'TCL 55S517 55-Inch 4K Ultra HD Roku Smart LED TV (2018 Model)',\
           'Samsung SM-N950UZKAXAA Galaxy Note8 (US Version) Factory Unlocked Phone - 6.3" Screen - 64GB - Midnight Black (U.S. Warranty)',\
           'Nokia 3.1 - Android One (Oreo) - 16 GB - Dual SIM Unlocked Smartphone (AT&T/T-Mobile/MetroPCS/Cricket/H2O) - 5.2" Screen - Blue - U.S. Warranty',\
           'Apple iPhone 7 32GB Unlocked, Black US Version',\
           'Microsoft Surface Pro 6 (Intel Core i5, 8GB RAM, 256GB) - Newest Version',\
           '2018 Newest Flagship Lenovo IdeaPad 330 15.6" HD Anti-glare Laptop, Intel Quad-Core Celeron N4100 4GB RAM 500GB HDD DVDRW 802.11ac HDMI Bluetooth Webcam USB 3.0 Win 10',\
           'Dell G5 Gaming Laptop 15.6" Full HD, Intel Core i7-8750H',\
           'Panasonic Microwave Oven NN-SN651B Black Countertop with Inverter Technology and Genius Sensor, 1.2 Cu. Ft, 1200W',\
           'Midea WHD-113FW1 Compact Reversible Double Door Refrigerator and Freezer, 3.1 Cubic Feet, White',\
           'Honeywell HCE323V Digital Ceramic Heater']

data=[]

for i in range(12):
    
    ## 从Amazon的商品名进入EBay搜索结果页
    title=titlelist[i]
    stitle = title.replace(' ','+')
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + stitle
    
    response = requests.get(url) 
    if response.status_code == 200:
        print("Success")
        results_page = BeautifulSoup(response.content,'lxml')
    else:
        print("Failure")
        
    ## 若没检索到商品，记录空字串    
    if results_page.find('h1',class_ = 'srp-controls__count-heading').string[0]=='0':
        data.append([i+1,'','','','',''])
    else:
        ## 检索到商品，记录第一个商品信息
        products_list = results_page.find_all('li',class_ = 's-item')[0]

        link = products_list.find('a').get('href')
        name = products_list.find('h3').text
        price = products_list.find('div',class_='s-item__detail s-item__detail--primary').text
        
        if products_list.find('div',class_='b-starrating'):
            rate = products_list.find('div',class_='b-starrating').text[:3]
        else:
            rate=''
        
        if products_list.find('span',class_='s-item__reviews-count'):
            num_text=products_list.find('span',class_='s-item__reviews-count').text
            num = re.search(r'(\d)+',num_text).group(1)
        else:
            num=''
        
        data.append([i+1,link,name,price,rate,num])
    
## 每次12*5存储进一张特别命名的csv表格
timename = time.strftime("%Y%m%d_%H", time.localtime()) 
with open('Ebay_'+timename+'.csv','w') as fp:
    writer=csv.writer(fp)
    writer.writerows(data)

'''
## 查看csv
with open('Ebay_'+timename+'.csv','r') as fp:
    r=csv.reader(fp)
    d=list(r)
''' 



