![Scapy logo](https://scrapy.org/img/scrapylogo.png)

# BukuKita Web Scraping with Scrapy

This is a web scraping project using Scrapy to extract data from Bukukita.com.

## About Scrapy

Scrapy is an open-source web scraping framework for Python. 
It is used to extract data from websites and can be used to extract structured data such as contact information, product details, or prices.

Scrapy provides an integrated way to follow links and extract data from multiple pages. 
It also provides support for handling common web scraping challenges such as handling cookies and sessions, handling redirects, and handling CAPTCHAs.

Scrapy is built on top of the Twisted asynchronous networking library and provides an extensible architecture for adding custom functionality. 
It also includes a built-in logging system, which can be used to track errors and monitor the progress of your spiders.

Scrapy can be used to scrape websites in a variety of formats, including HTML, XML, and JSON. 
It can be used to scrape websites built with a variety of technologies, including JavaScript, Flash, and AJAX.


## Spider's functionality
Scrapy will use a python code called "Spider" to crawl through the website. The spider in this porject is called buku and the functions are defined in file buku.py. The spider will start by making an HTTP request to the Bukukita website. Once the spider receives the response it will extract the following data for each book:

1. source	
2. Title
3. ISBN No.	
4. Publisher	
5. Publish Date	
6. No of page	
7. Weight(g)
8. Cover Type
9. Dimension
10. Category
11. Bonus	
12. Language	
13. Stock Location

The spider will continue to follow the links on the page and extract the data for each book it finds.


## Group Member
1. LEE MING QI

2. NUR IRDINA ALIAH BINTI ABDUL WAHAB

3. SINGTHAI SRISOI

4. AMIRAH RAIHANAH BINTI ABDUL RAHIM


