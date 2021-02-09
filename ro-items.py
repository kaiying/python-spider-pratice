# import
import requests
from bs4 import BeautifulSoup
import json

# 
# id = str(13417)
id = str(13417)
url = 'https://rd.fharr.com/item-' + id + '.html'

# print(url)

# sequences = [0, 1, 2, 3, 4, 5]
# sequences = range(0, 1)
sequences = [1, 13417, 585]
for i in sequences:
  id = str(i)
  url = 'https://rd.fharr.com/item-' + id + '.html'
  print(url)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  # Empty Page
  result = soup.find(id='search-sys').find('h4', 'alert-heading')
  if result is not None:
    continue

  # item
  result = soup.find('table').find_all('td')

  item_name = result[0].text.replace('臺灣', '').strip();

  json_object = {
    'id': id,
    'name': item_name
    }
  print('============');
  # 圖片
  # print(result[1]);
  # print('============');
  print(result[2].find_all('p'));
  for idx, element in enumerate(result[2].find_all('p')):
    print(element)
  # print(result, len(result));

  print(json_object);