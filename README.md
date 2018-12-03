IEOR 4501 Sec-001 Project
Group Name: PaulFans


Group Members: Xinyue Li (xl2804), Zixuan Li (zl2713)，Wenshan Liang (wl2676), Dawei Zhang (dz2386)


Project Description: 

In this project, we aim to create a UI for price comparison, so that customers are able to choose targeted products at a relatively low price at proper time and proper shopping website. Each of us works on a certain online shopping website (Amazon, Walmart, Ebay and NewEgg) to get a specific product information (e.g. price, reviews, rating) through web scraping. After collecting data of a targeted product, we create a UI, which visualizes fluctuation and trend of product price with line graphs and displays other product information during the past few days on various shopping platforms. Moreover, we prepare a simulated database which contains relevant information of 10 speficic products to help users better understand and experience our program. 
 

Development Flow: 

1. Web scraping
Target: Information of M kinds of products on N online shopping platforms.
Frequency: Every six hours.
Data dimension: M Products * N Online platform *  T hours.

2. Data analytics
Ploting time-series information of the target product on each platform.
Showing similar products' information for the target product.


Installation Instructions:

First, you need to clone the repo using the url we submitted.

Then import Python packages, which are listed in requirements.txt




Run Instructions:

To start our program, you can first open and run the "scraping.py" file. After running this file, you will get a csv file showing information of 10 products from four online shopping websites at one point in time and you can get as many csv files as you want if you keep running the scraping.py file. To help you check our program, we prepare the simulated database called "Database" that contains around 120 csv files dating from 11-01-2018. Then, you can find and run a py file named "Database and Plotting.py". This py file will aggregate all these 120 csv files into a whole database file, create the "database.csv" file, plot the trend of product price with line graphs from four shopping websites and display other information at a certain time on certain day. Last but not least, you can open the "GUI" file, select one of the links of 10 products and choose start date or variables you want to see. From our well-designed UI, you are able to see the name, link, price trend, comment number and ratings of the product on four online shopping platform. Just take a look at this information and decide when and where to buy the product!


