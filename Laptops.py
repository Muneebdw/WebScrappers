from bs4 import BeautifulSoup
import pandas as pd
from requests import get

site = get('http://www.mega.pk/laptop/')
soup = BeautifulSoup(site.content,"html.parser")
items = soup.find_all(class_='detailer')
price = soup.find_all(class_='cat_price')
i= list()
price =[pr.get_text() for pr in price]

c=0;
for x in items:
    print(x.get_text())
    print(price[c])
    price[c]=price[c].strip()
    c= c+1

specs= [pt.get_text() for pt in items]

laptop = pd.DataFrame({
    "Specs":specs,
    "Price":price

    })
laptop.to_csv('Laptops.csv')
