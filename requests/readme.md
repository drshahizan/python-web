![Requests](https://media.licdn.com/dms/image/C4E12AQFncA0AxujAng/article-cover_image-shrink_600_2000/0/1520086554238?e=2147483647&v=beta&t=ZvpayB6CfpbF7YCWJlynIyYqkBR23iRZpj2kd2XDR5E)

# **Web Scrapping (Requests)**

**Group 7**: No Name

**Group Members**:
<table>
  <tr>
    <th>Name</th>
    <th>Matric</th>
  </tr>
  <tr>
    <th>Madina Suraya binti Zharin</th>
    <th>A20EC0203</th>
  </tr>
  <tr>
    <th>Nur Izzah Mardhiah binti Rashidi</th>
    <th>A20EC0116</th>
  </tr>
    <tr>
    <th>Tan Yong Sheng</th>
    <th>A20EC0157</th>
  </tr>
    <tr>
    <th>Chloe Racquelmae Kennedy</th>
    <th>A20EC0026</th>
  </tr>
</table>

## About Requests
Using requests library, we can fetch the content from the URL given. Requests library is the best choice if we just start with web scraping and have access to an API. <b>The requests library will make a GET request to a web server, which will download the HTML contents of a given web page for us.</b>

- It is easy to understand and does not require much practice to master. 
- Requests also minimizes the need to include query strings in your URLs manually. 
- It also supports authentication modules and handles cookies and sessions with excellent stability.

## Purpose

However, using requests library solely is not enough to do web scraping. Hence, we need libraries that can parse the document. In this notebook, we use the <b>Beautiful Soup library to parse this document, and extract the text from the div tag.</b>

We chose [Puma website](https://my.puma.com/my/en/women/shoes/sneakers) to perform web scraping since it is the Chinese New Year season, and they offer sale. Therefore, we would like to see if there is any interesting data **(Product Name, Price New, Price Old)** related to their sneakers. 

## Results
There are 36 items that we had extracted. However, some of them is duplicates and contains null values. 

- Product Name 

- Price New = price after CNY sale discount

- Price Old = the original price without any discount

We then perform some data cleaning before store the data into an Excel file which we also uploaded entitled [puma_sneakers_women_sale.csv](https://github.com/drshahizan/python-web/blob/main/requests/puma_sneakers_women_sale.csv) file. 
