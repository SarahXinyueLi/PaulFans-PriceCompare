
# coding: utf-8

# In[9]:


from lxml import html
import csv
import os
import requests
from time import sleep
from random import randint
import urllib3

urllib3.disable_warnings()

def ReadAsin():
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
                
                    RAW_NAME = doc.xpath(XPATH_NAME)
               
                    NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
                    return NAME
            
                elif response.status_code==404:
                    break

        except Exception as e:
            print(e)
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
     #'B07987KQBN','B07536MYBQ','B07DDD8PNQ','B01LYT95XR', 'B07HZNKGDV','B07DN2JG5T','B07GM4VHNP','B00FRD0PNC','B00MVVIMTW','B00KNBKB64'           
    extracted_data = []

    for i in AsinList:

        url = "http://www.amazon.com/dp/" + i
        # Calling the parser
        parsed_data = parse(url)
        if parsed_data:
            extracted_data.append(parsed_data)
    return extracted_data
if __name__ == "__main__":
    ReadAsin()


# In[ ]:


print(ReadAsin())

