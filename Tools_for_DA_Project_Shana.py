
# coding: utf-8

# # Sample products & links

# 【1】Toshiba 43LF621U19 43-inch 4K Ultra HD Smart LED TV HDR - Fire TV Edition
# https://www.amazon.com/Toshiba-43LF621U19-43-inch-Ultra-Smart/dp/B07D4F2P26/ref=sr_1_8?s=tv&ie=UTF8&qid=1541737557&sr=1-8&keywords=tv
# 
# 【2】Samsung UN50NU7100 50" (UN50NU7100FXZA) 
# https://www.amazon.com/Samsung-UN50NU7100-UN50NU7100FXZA-Mountable-Bluetooth/dp/B07DD1YS56/ref=sr_1_1?ie=UTF8&qid=1541643591&sr=8-1&keywords=Samsung+NU7100+50%22+TV+UN50NU7100FXZA
# 
# 【3】TCL 55S405 55-Inch 4K Ultra HD Roku Smart LED TV (2017 Model)
# https://www.amazon.com/TCL-55S405-55-Inch-Ultra-Smart/dp/B01MTGM5I9/ref=sr_1_2_sspa?s=tv&ie=UTF8&qid=1541737439&sr=1-2-spons&keywords=tv&psc=1
# 
# 【4】Samsung SM-N950UZKAXAA
# https://www.amazon.com/Samsung-SM-N950UZKAXAA-Version-Factory-Unlocked/dp/B07536MYBQ/ref=sr_1_4?s=wireless&ie=UTF8&qid=1541726067&sr=1-4&keywords=galaxy+note
# 
# 【5】Nokia 3.1 - Android One (Oreo) - 16 GB - Dual SIM Unlocked Smartphone (AT&T/T-Mobile/MetroPCS/Cricket/H2O) - 5.2" Screen - Blue - U.S. Warranty
# https://www.amazon.com/Nokia-3-1-Unlocked-Smartphone-T-Mobile/dp/B07DDD8PNQ/ref=sr_1_6?s=mobile-apps&ie=UTF8&qid=1541724798&sr=8-6&keywords=nokia
# 
# 【6】Apple iPhone 7 32GB unlocked black
# https://www.amazon.com/Apple-iPhone-Unlocked-Black-Version/dp/B01LYT95XR/ref=sr_1_8?s=wireless&ie=UTF8&qid=1541725701&sr=1-8&keywords=Apple+iPhone+7%2C+32GB
# 
# 【7】Microsoft surface pro6 256GB
# https://www.amazon.com/Microsoft-Surface-Intel-Core-256GB/dp/B07HZNKGDV/ref=sr_1_3?ie=UTF8&qid=1541733553&sr=8-3&keywords=microsoft+surface+pro+6
# 
# 【8】Lenovo yoga 730 convertible
# https://www.amazon.com/Flagship-Lenovo-i5-8250U-Bluetooth-Thunderbolt/dp/B07J1T63JG/ref=sr_1_1_sspa?s=pc&ie=UTF8&qid=1541733175&sr=1-1-spons&keywords=lenovo+yoga+730&psc=1
# 
# 【9】Dell G5 Gaming Laptop 15.6" Full HD, Intel Core i7-8750H
# https://www.amazon.com/Premium-Dell-i7-8750H-Keyboard-Bluetooth/dp/B07GM4VHNP/ref=sr_1_1?ie=UTF8&qid=1541732861&sr=8-1&keywords=Dell+G5+Gaming+Laptop+15.6%22+Full+HD%2C+Intel+Core+i7-8750H
# 
# 【10】
# https://www.amazon.com/AVANTI-RM4416B-Refrigerator-Energy-Compliant/dp/B01CMW3ZP0/ref=sr_1_1?s=appliances&ie=UTF8&qid=1541726380&sr=1-1&keywords=avanti+RM4416B&dpID=51hgym9oLKL&preST=_SY300_QL70_&dpSrc=srch
# 
# 【11】
# https://www.amazon.com/GE-GFW480SSKWW-White-Stackable-Washer/dp/B06XKTPB45/ref=sr_1_cc_1?s=aps&ie=UTF8&qid=1541724969&sr=1-1-catcorr&keywords=ge+GFW480SSKWW
# 
# 【12】
# https://www.amazon.com/Panasonic-Microwave-NN-SN651B-Countertop-Technology/dp/B00FRD0PNC/ref=sr_1_4?s=home-garden&ie=UTF8&qid=1541723725&sr=1-4&keywords=panasonic+microwave+NN-SN651B&dpID=41-d0ePOmZL&preST=_SY300_QL70_&dpSrc=srch
# 

# # Imports

# In[1]:


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


# # Keywords preparation

# In[20]:


# seperate keywords

# connect with %20

keywords = 'Apple%20iPhone%207%2032GB%20Unlocked%2C%20Black%20US%20Version'
search_url = 'https://www.walmart.com/search/?query=' + keywords


# # Web Scraping - Walmart

# In[22]:


def get_web_scrap_result(url):
    response = requests.get(url) 
    if response.status_code == 200:
        print("Success")
        results_page = BeautifulSoup(response.content,'lxml')
    else:
        print("Failure")
    return results_page


# In[23]:


results_page = get_web_scrap_result(search_url)
print(results_page.prettify())


# ### only consider the first link as the target similar product for now

# In[24]:


def get_top_product_info(results_page):
    products_list = results_page.find_all('div',class_ = 'search-result-product-title listview')[0]
    product_link = products_list.find('a').get('href')
    product_link_full = 'https://www.walmart.com' + product_link
    return product_link_full


# In[25]:


product_link_full = get_top_product_info(results_page)
product_link_full


# In[39]:


def get_product_price(product_link_full):
    product_result_page = get_web_scrap_result(product_link_full)
    # get price
    try:
        price = product_result_page.find('span',class_ = "price-characteristic").get('content')
    except:
        print('Cannot find price tag')
    # get rating
    overall_rating = product_result_page.find('span',class_ = "ReviewsHeader-rating").get_text()
    overall_rating = float(overall_rating[:3])
        
    return ?????


# In[30]:


product_result_page = get_product_price(product_link_full)


# In[42]:


overall_rating = product_result_page.find('span',class_ = "ReviewsHeader-rating").get_text()
overall_rating = float(overall_rating[:3])


# In[88]:


def get_review(product_result_page):
    reviews_list = product_result_page.find_all('div',class_ = "review")
    review_title_list = list()
    review_content_list = list()
    for review in reviews_list:
        # get review title
        try:
            review_title = review.find('div',class_="review-title").get_text()
        except:
            review_title = ''
        review_title_list.append(review_title)
        
        # get review content
        try:
            review.find('div',class_='collapsable-content-container').get_text()
            review_content_list.append(review.find('div',class_='collapsable-content-container').get_text())
        except:
            review_content_list.append('')

    return review_title_list,review_content_list


# In[89]:


review_title_list,review_content_list = get_review(product_result_page)


# In[74]:


reviews_list[0]

