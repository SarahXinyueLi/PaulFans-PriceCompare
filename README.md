# PaulFans-PriceCompare
https://docs.google.com/document/d/18z6eaY8qy6jQ2RiHLE2rYUx01dZ3vLVumd1vl-QqcHs/edit?ts=5bb646e9

IEOR 4501 Sec-001 Project
Group Name: PaulFans


Group Members: Xinyue Li (xl2804), Zixuan Li (zl2713)，Wenshan Liang (wl2676), Dawei Zhang (dz2386)


Project Description: In this project, we aim to create a UI for price comparison, so that customers are able to choose targeted products at a relatively low price at proper time and proper shopping website. Each of us worked on a certain online shopping website (Amazon, Walmart, Ebay and NewEgg) to get a specific products information (e.g. price, reviews, rating) through web scraping. After collecting data of a targeted product, we created a UI, which visualizes fluctuation and trend of product price with line graphs and displays other product information during the past few days on various shopping platforms. 






Project Objective: We aim to create a UI for price comparison, so that customers are able to choose targeted products at a relatively low price at proper time and proper shopping website.

Key Functions: 

1. Scraping daily products information (e.g. price, reviews) from comparable online shopping platforms. 

2. Visualizing fluctuation and trend of price, the number of reviews, etc. during the past few days on various shopping platforms.

3. Displaying different price information of same product from different shopping websites in Python.


Development Flow: 

1. Web scraping
Target: Information of M kinds of products on N online shopping platforms.
Frequency: Daily.
Data dimension: M Products * N Online platform *  T Days.

2. Data analytics
Ploting time-series information of the same product on each platform.
Computing daily price percentage change and variance.
Recommend the platform wtih the lowest price for each product.
