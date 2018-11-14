# PaulFans-PriceCompare
Group Name: PaulFans

https://docs.google.com/document/d/18z6eaY8qy6jQ2RiHLE2rYUx01dZ3vLVumd1vl-QqcHs/edit?ts=5bb646e9

Group Members: Wenshan Liang (wl2676), Dawei Zhang (dz2386), Xinyue Li (xl2804), Zixuan Li (zl2713)

Project Purpose: Helping customers purchase targeted products at a relatively low price by choosing the right time and right shopping website.

Core Function: 

1. Scraping daily product information (e.g. price, reviews) from comparable online shopping platforms. 

2. Visualizing fluctuation and trend of price, the number of reviews, etc. during the past few days.

3. Displaying to users the difference of price in same product from different shopping websites.


Development Flow: 
1. Web scraping. 
Target: Information of M kinds of products on N online shopping platforms.
Frequency: Daily.
Data dimension: M Products * N Online platform *  T Days.

2. Data analytics. 
Ploting time-series information of the same product on each platform.
Computing change percentage and variance.
Select the platform of lowest price for the same product.
