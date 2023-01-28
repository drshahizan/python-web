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

![Requests](https://media.licdn.com/dms/image/C4E12AQFncA0AxujAng/article-cover_image-shrink_600_2000/0/1520086554238?e=2147483647&v=beta&t=ZvpayB6CfpbF7YCWJlynIyYqkBR23iRZpj2kd2XDR5E)

## About Requests
Using requests library, we can fetch the content from the URL given and Beautiful Soup library helps to parse it and fetch the details the way we want. Requests library is the best choice if you just start with web scraping and have access to an API. It is easy to understand and does not require much practice to master. Requests also minimizes the need to include query strings in your URLs manually. It also supports authentication modules and handles cookies and sessions with excellent stability.

## Results 
Since the CNY sale, we wanted to web scrape this [Puma website](https://my.puma.com/my/en/women/shoes/sneakers) to see any major differences in price. There will be three metadata that we want to get which are **Product Name, Price New, and Price Old.** 

Price New = price after CNY sale discount

Price Old = the original price without any discount

The results are saved in the [puma_sneakers_women_sale.csv](https://github.com/drshahizan/python-web/blob/main/requests/puma_sneakers_women_sale.csv) file. 
