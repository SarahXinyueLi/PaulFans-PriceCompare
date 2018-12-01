
# coding: utf-8

# In[5]:


from lxml import html
import csv
import os
import requests
from time import sleep
from random import randint

def parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
    
    try:
        # Retrying for failed requests
        for i in range(20):
            # Generating random delays
            sleep(randint(1,3))
            # Adding verify=False to avold ssl related issues
            response = requests.get(url, headers=headers, verify=False)

            if response.status_code == 200: 
                doc = html.fromstring(response.content)
                XPATH_NAME = '//h1[@id="title"]//text()'
                XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
                XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
                XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
                XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
                XPATH_COMMENTS = '//*[@id="acrCustomerReviewText"]//text()'
                XPATH_RATING='//div[@id="averageCustomerReviews"]/span/span/span/a//text()'

                RAW_NAME = doc.xpath(XPATH_NAME)
                RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
                RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
                RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
                RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
                RAW_RATING = doc.xpath(XPATH_RATING)
                RAW_COMMENTS = doc.xpath(XPATH_COMMENTS)

                NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
                SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
                CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
                ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
                AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
                RATING=''.join(RAW_RATING).strip() if RAW_RATING else None
                COMMENTS = ''.join(RAW_COMMENTS).strip() if RAW_COMMENTS else None

                if not ORIGINAL_PRICE:
                    ORIGINAL_PRICE = SALE_PRICE
                # retrying in case of captcha
                if not NAME:
                    raise ValueError('captcha')

                data = {
                    'NAME': NAME,
                    'SALE_PRICE': SALE_PRICE,
                    'CATEGORY': CATEGORY,
                    'ORIGINAL_PRICE': ORIGINAL_PRICE,
                    'AVAILABILITY': AVAILABILITY,
                    'COMMENTS':COMMENTS,
                    'RATING':RATING,
                    'URL': url,
                }
                return data
            
            elif response.status_code==404:
                break

    except Exception as e:
        print(e)

def ReadAsin():
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))
    AsinList = ['B07D4F2P26',
                'B073JP6WK4',
                'B07987KQBN',
                'B07536MYBQ',
                'B07DDD8PNQ',
                'B01LYT95XR',
                'B07HZNKGDV',
                'B07DN2JG5T',
                'B07GM4VHNP',
                'B00FRD0PNC',
                'B00MVVIMTW',
                'B00KNBKB64' ]
    extracted_data = []

    for i in AsinList:
        url = "http://www.amazon.com/dp/" + i
        print("Processing: " + url)
        # Calling the parser
        parsed_data = parse(url)
        if parsed_data:
            extracted_data.append(parsed_data)
    import time 
    tttmmm=time.time()
    ff=time.ctime(tttmmm)+'.csv'

    # Writing scraped data to csv file
    with open(ff, 'w') as csvfile:
        fieldnames = ['NAME','SALE_PRICE','CATEGORY','ORIGINAL_PRICE','AVAILABILITY','COMMENTS','RATING','URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()    
        for data in extracted_data:
            writer.writerow(data)

if __name__ == "__main__":
    ReadAsin()

