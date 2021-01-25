from bs4 import BeautifulSoup
import pandas as pd
from requests import get

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'} #header to establish secure connection
url = 'https://en.wikipedia.org/wiki/List_of_national_capitals' #provide required url
page = get(url,headers=headers)   #get page  
soup = BeautifulSoup(page.content, "html.parser")  #initiliaze soup
table = soup.find_all('table')[1]   #get the table from page
rows = table.find_all('tr')   #get the rows from the table
row_list = list() #initiliaze a list 

for tr in rows:   #loop to go through all rows
    td = tr.find_all('td')  #used to search inside the row
    row = [i.text for i in td]   #extracts the texts from all the rows 
    row_list.append(row)    #appends row
df_bs = pd.DataFrame(row_list,columns=['City','Capital','Notes'])  #makes a dataframe
df_bs.set_index('Country',inplace=True)  #sets index
df_bs.to_csv('beautifulsoup.csv') #saves as csv file