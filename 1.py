import requests
from bs4 import BeautifulSoup
import json
response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, "html.parser")

# foreach
# sequences = [0, 1, 2, 3, 4, 5]
sequences = range(11)
for i in sequences:
    print(i)


##### write file sample
# f = open('test.txt', 'a')
# f.write(soup.prettify())
# f.close()

#### 抓取網頁
#  print(soup.prettify())  #輸出排版後的HTML內容
#result = soup.find("h3")
#result = soup.find_all("h3", itemprop="headline", limit=3)
#result = soup.find_all(["h3", "p"], limit=2)
#print(result)

