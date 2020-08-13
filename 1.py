import requests
from bs4 import BeautifulSoup
response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, "html.parser")

#print(soup.prettify())  #輸出排版後的HTML內容

#result = soup.find("h3")
#result = soup.find_all("h3", itemprop="headline", limit=3)
result = soup.find_all(["h3", "p"], limit=2)
print(result)