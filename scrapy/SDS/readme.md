![Scapy logo](https://scrapy.org/img/scrapylogo.png)

# Web Scraping on Book Depository using Scrapy

We perform web scraping on the Book Depository website using Scrapy to extract the book information related to big data. Only the first page of the search result is extracted. Then, the data is cleaned and exported to a csv file. As a result, 30 rows of big data books information including their title, author, published date, format and price are successfully scraped and stored in the output `big_data_books.csv` file.

**Group Members:**

<table width = 700>
  <tr>
    <th>Name</th>
    <th>Matric</th>
  </tr>
  <tr>
    <th>ONG HAN WAH</th>
    <th>A20EC0129</th>
  </tr>
  <tr>
    <th>GOO YE JUI</th>
    <th>A20EC0191</th>
  </tr>
    <tr>
    <th>MAIZATUL AFRINA SAFIAH BINTI SAIFUL AZWAN</th>
    <th>A20EC0204</th>
  </tr>
    
</table> 

---

# About Scrapy

Scrapy is a Python web scraping framework. It provides a pre-defined set of methods and classes for crawling websites and extracting structured data, such as data for items like products, prices, reviews, etc. Scrapy is built on top of the Twisted asynchronous networking library, which means that it can handle large amounts of data and high concurrency without blocking the execution of the program.

Scrapy has several built-in features like:

Support for handling cookies and user-agents
Built-in support for handling redirects
Built-in support for handling forms
Built-in support for handling common HTTP status codes
Built-in support for extracting data from HTML and XML
Built-in support for generating CSV, JSON, or XML output
Scrapy is an open-source project, so you can use it for free and make any modifications you need. It is widely used for data mining, data extraction, and web scraping. You can use Scrapy to scrape data from websites, process it and store it in any format you want.

## Installation guide for scrapy
### Supported Python versions
Scrapy requires Python 3.7+, either the CPython implementation (default) or the PyPy implementation (see Alternate Implementations).

### Installing Scrapy
You can install Scrapy and its dependencies from PyPI with:

``` pip install Scrapy ```

---

# About Dataset
<table>
  <tr>
    <th>Columns</th>
    <th>Description</th>
  </tr>
  <tr>
    <th>Title</th>
    <th>Title of the book</th>
  </tr>
  <tr>
    <th>Author</th>
    <th>Author of the book</th>
  </tr>
  <tr>
    <th>Published date</th>
    <th>The date of the book published</th>
  </tr>
  <tr>
    <th>Format</th>
    <th>Format of the book</th>
  </tr>
  <tr>
    <th>Price</th>
    <th>Price of the book</th>
  </tr>
  
</table>
