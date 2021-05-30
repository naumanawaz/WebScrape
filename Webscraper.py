# import library
from bs4 import BeautifulSoup
import json # for parsing data
from pandas import DataFrame as df
import requests# Request to website and download HTML contents

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
base_url = "https://dev-test.hudsonstaging.co.uk/"

r = requests.get(base_url,headers=header)


if r.status_code == 200:
  soup = BeautifulSoup(r.text, 'html.parser')
  products = soup.find_all(attrs={"product-tile"})
  result=[]
  for product in products:
    productName=product.find('p', attrs={'class':'product-name'}).text
   # price=product.find('p',attrs={'class':'details'})

    link = base_url + product.find('img')['src']
    single ={'Product':productName,'Metadata':{'Image_url':link}}
    #,'Price':picture 'Metadata':stars,
    result.append(single)
    with open('Products.json','w') as f:
      json.dump(result,f,indent=4)
else:
  print(req.status_code)


