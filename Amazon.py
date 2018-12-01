
# coding: utf-8

# In[30]:


from lxml import html
import csv,os,json
import requests
from time import sleep

def parse(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url,headers=headers)
    print(page)
    for i in range(20):
        sleep(10)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
            XPATH_COMMENTS = '//*[@id="acrCustomerReviewText"]//text()'
            #//*[@id="dp-summary-see-all-reviews"]/h2
            #//*[@id="acrCustomerReviewText"]
            XPATH_RATING='//div[@id="averageCustomerReviews"]/span/span/span/a//text()'
            #//div[@id="averageCustomerReviews"]/span/span/span/a
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
#//*[@id="dp-summary-see-all-reviews"]   //*[@id="dp-summary-see-all-reviews"]/h2
            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAW_RATING = doc.xpath(XPATH_RATING)
            RAW_COMMENTS = doc.xpath(XPATH_COMMENTS)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)

            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
            RATING=''.join(RAW_RATING).strip() if RAW_RATING else None
            COMMENTS = ''.join(RAW_COMMENTS).strip() if RAW_COMMENTS else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
            '''
            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE
            #retrying in case of caotcha
            if not NAME :
                raise ValueError('captcha')
            '''
            data = {
                    'NAME':NAME,
                    'SALE_PRICE':SALE_PRICE,
                    'CATEGORY':CATEGORY,
                    'ORIGINAL_PRICE':ORIGINAL_PRICE,
                    'AVAILABILITY':AVAILABILITY,
                    'COMMENTS':COMMENTS,
                    'RATING':RATING,
                    'URL':url,
                    }

            return data
        except Exception as e:
            print (type(data))
        with open('/Users/zixuan/Desktop/Amazon.csv', 'w', newline='') as f:  # file_path 是 csv 文件存储的路径
            fieldnames = ['Attributes', 'Value']          # 假设有两列
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()                     # 写入头部，即设置列名
            for item in data:                        # dict 是需要写入的字典
                writer.writerow(item)
            


# In[31]:


parse('https://www.amazon.com/Nokia-3-1-Unlocked-Smartphone-T-Mobile/dp/B07DDD8PNQ/ref=sr_1_6?s=mobile-apps&ie=UTF8&qid=1541724798&sr=8-6&keywords=nokia')


# In[20]:


import csv
url=[https://www.amazon.com/Toshiba-43LF621U19-43-inch-Ultra-Smart/dp/B07D4F2P26/ref=sr_1_8?s=tv&ie=UTF8&qid=1541737557&sr=1-8&keywords=tv,https://www.amazon.com/Samsung-Electronics-UN32M4500A-32-Inch-Smart/dp/B073JP6WK4/ref=sr_1_acs_bss_1_1?s=tv&ie=UTF8&qid=1543333023&sr=1-1-acs&keywords=samsung+tv,https://www.amazon.com/TCL-55S517-55-Inch-Ultra-Smart/dp/B07987KQBN/ref=sr_1_1_sspa?s=tv&ie=UTF8&qid=1543351513&sr=1-1-spons&keywords=tcl+tv&psc=1,https://www.amazon.com/Samsung-SM-N950UZKAXAA-Version-Factory-Unlocked/dp/B07536MYBQ/ref=sr_1_4?s=wireless&ie=UTF8&qid=1541726067&sr=1-4&keywords=galaxy+note,https://www.amazon.com/Nokia-3-1-Unlocked-Smartphone-T-Mobile/dp/B07DDD8PNQ/ref=sr_1_6?s=mobile-apps&ie=UTF8&qid=1541724798&sr=8-6&keywords=nokia,https://www.amazon.com/Apple-iPhone-Unlocked-Black-Version/dp/B01LYT95XR/ref=sr_1_8?s=wireless&ie=UTF8&qid=1541725701&sr=1-8&keywords=Apple+iPhone+7%2C+32GB,https://www.amazon.com/Microsoft-Surface-Intel-Core-256GB/dp/B07HZNKGDV/ref=sr_1_3?ie=UTF8&qid=1541733553&sr=8-3&keywords=microsoft+surface+pro+6,https://www.amazon.com/Flagship-Lenovo-Anti-glare-Quad-Core-Bluetooth/dp/B07DN2JG5T/ref=sr_1_4?ie=UTF8&qid=1543335827&sr=8-4&keywords=Lenovo+Laptop+IdeaPad+330,https://www.amazon.com/Premium-Dell-i7-8750H-Keyboard-Bluetooth/dp/B07GM4VHNP/ref=sr_1_1?ie=UTF8&qid=1541732861&sr=8-1&keywords=Dell+G5+Gaming+Laptop+15.6%22+Full+HD%2C+Intel+Core+i7-8750H,https://www.amazon.com/Panasonic-Microwave-NN-SN651B-Countertop-Technology/dp/B00FRD0PNC/ref=sr_1_4?s=home-garden&ie=UTF8&qid=1541723725&sr=1-4&keywords=panasonic+microwave+NN-SN651B&dpID=41-d0ePOmZL&preST=_SY300_QL70_&dpSrc=srch,https://www.amazon.com/WHD-113FW1-Compact-Reversible-Refrigerator-Freezer/dp/B00MVVIMTW/ref=sr_1_1?ie=UTF8&qid=1543334614&sr=8-1&keywords=Midea+WHD-113FW1+3.1,https://www.amazon.com/d/Space-Heaters-Accessories/Honeywell-HCE323V-Digital-Ceramic-Heater/B00KNBKB64/ref=sr_1_2_sspa?s=home-garden&ie=UTF8&qid=1543337061&sr=1-2-spons&keywords=Lasko+Ceramic+Tower+Heater+with+Digital+Display+%26+Remote+Control&psc=1]
for i in url:
import csv

with open(Amazon.csv, 'w', newline='') as f:  # file_path 是 csv 文件存储的路径
    fieldnames = ['Attributes', 'Value']          # 假设有两列
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()                     # 写入头部，即设置列名
    for item in dict:                        # dict 是需要写入的字典
        writer.writerow(item)

