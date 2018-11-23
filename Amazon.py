
# coding: utf-8

# In[13]:


from lxml import html
import csv,os,json
import requests
from time import sleep

def parse(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url,headers=headers)
    for i in range(20):
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
            XPATH_RATING = '//*[@id="reviewsMedley"]/div/div[1]/div[1]/div/div/div[2]/div/span/span/a/span//text()'
            XPATH_COMMENTS='//h2[@id="dp-summary-see-all-reviews"]//text()'
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

            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE
            #retrying in case of caotcha
            if not NAME :
                raise ValueError('captcha')

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
            print (e)


# In[ ]:


parse("https://www.amazon.com/Toshiba-43LF621U19-43-inch-Ultra-Smart/dp/B07D4F2P26/ref=sr_1_8?s=tv&ie=UTF8&qid=1541737557&sr=1-8&keywords=tv")

