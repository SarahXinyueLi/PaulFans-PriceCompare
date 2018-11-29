
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

#First, we enter the keywords for certain products

def get_NewEgg(initial_keywords):
    #initial_keywords= input("Please enter the keywords : ")
    initial_keywords = initial_keywords.split()
    initial_keywords = initial_keywords[:len(initial_keywords)//3]
    keywords = " ".join(str(x) for x in initial_keywords)
    
    url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=" + keywords + "&N=-1&isNodeId=1"
    response = requests.get(url)

    #We want the status code to be 200
    if not response.status_code == 200:
        return "Requests Failed"

    try:
        results_page = BeautifulSoup(response.content,'lxml')

        if results_page.find_all('span',class_="result-message-error"):
            
            # if the product does not exist, return '-'
            Results_ = ['-','-','-','-','-']
            return Results_

        else:
            new_url = results_page.find_all('a',class_="item-title")[0].get('href')
            new_response = requests.get(new_url)
            
            #We want the status code to be 200
            if not new_response.status_code == 200:
                return "Requests Failed"
            
            # Get certain product information through web scraping
            try:
                new_results_page = BeautifulSoup(new_response.content,'lxml')
                new_title = results_page.find_all('a',class_="item-title")[0].get_text().strip().split('\n')
                new_price = results_page.find_all('li',class_="price-current")[0].get_text()
                new_price = new_price.split('\xa0')[0].split('\n')[-1]
                
                # if the review and rating do not exist, return '-'
                if new_results_page.find('a',class_="first_review"):
                    number_of_product_rating = '-'
                    new_rating = '-'
                
                # Get product review and information
                else:
                    number_of_product_rating = new_results_page.find('span',itemprop="reviewCount").get_text()
                    new_rating = new_results_page.find_all('span',class_="print")[0].get_text()[0]
                
                Results = [new_title,new_price,number_of_product_rating,new_rating,new_url]
                
                
                return Results

            except:
                return Results_

    except:
        return ['-','-','-','-','-']
    


# In[2]:


# test the function with a specific product list
product_list = ['Toshiba 43LF621U19 43-inch 4K Ultra HD Smart LED TV HDR - Fire TV Edition',
               'Samsung Electronics UN32M4500A 32-Inch 720p Smart LED TV (2017 Model)',
               'TCL 55S517 55-Inch 4K Ultra HD Roku Smart LED TV (2018 Model)',
               'Samsung SM-N950UZKAXAA Galaxy Note8 (US Version) Factory Unlocked Phone - 6.3" Screen - 64GB - Midnight Black (U.S. Warranty)',
               'Nokia 3.1 - Android One (Oreo) - 16 GB - Dual SIM Unlocked Smartphone (AT&T/T-Mobile/MetroPCS/Cricket/H2O) - 5.2" Screen - Blue - U.S. Warranty',
               'Apple iPhone 7 32GB Unlocked, Black US Version',
               'Microsoft Surface Pro 6 (Intel Core i5, 8GB RAM, 256GB) - Newest Version',
               '2018 Newest Flagship Lenovo IdeaPad 330 15.6" HD Anti-glare Laptop, Intel Quad-Core Celeron N4100 4GB RAM 500GB HDD DVDRW 802.11ac HDMI Bluetooth Webcam USB 3.0 Win 10',
               'Dell G5 Gaming Laptop 15.6" Full HD, Intel Core i7-8750H',
               'Panasonic Microwave Oven NN-SN651B Black Countertop with Inverter Technology and Genius Sensor, 1.2 Cu. Ft, 1200W',
               'Midea WHD-113FW1 Compact Reversible Double Door Refrigerator and Freezer, 3.1 Cubic Feet, White',
               'Honeywell HCE323V Digital Ceramic Heater']


import csv
import time
from time import sleep

# Get a list of data containing information from product list above
data = [['Name','Price','Comments','Rating','Link']]
for i in product_list:
    sleep(1)
    data.append(get_NewEgg(i))

# create a csv file recording the information    
timename = time.strftime("%Y%m%d__%H", time.localtime())
with open('NewEgg' + timename + '.csv','w') as fp:
    writer = csv.writer(fp)
    writer.writerows(data)

