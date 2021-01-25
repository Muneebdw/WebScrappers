url = 'https://www.amazon.com/s?k=gaming+laptops&ref=nb_sb_noss'
url2 = 'https://www.esquire.com/entertainment/movies/g29500577/best-movies-of-2020/'
url3 = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
url4 = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
from bs4 import BeautifulSoup
import pandas as pd
from requests import get
"""
#Request can be used to download a web page
d1 = get(url3)
print(d1.status_code)  #code starts with 2 success else 4 or 5 error
print(d1.content) #prints downloaded page content

#We can use beautifulsoup to parse through html documents / websites online
soup = BeautifulSoup(d1.content, "html.parser")
print(soup.prettify()) #this formats the html code into a more pretty way

soup.find_all('p') #find all tags with argument
soup.find_all('p')[0].get_text() #.get_text() to get the text inside the tag/container

soup.find('p')  #Returns the first instance of the argument tag


page = get(url3)
soup = BeautifulSoup(page.content,"html.parser") #initializes the soup with content
print(soup.find_all('p', class_='outer-text'))#searches for tags with sent argument with class named as argument
print(soup.find_all(id = 'first')) #we can also search by id
soup.select("div p")  #search for all p tags inside div 
#"""


#implementation

page = get(url4)
soup = BeautifulSoup(page.content, "html.parser")
forecast = soup.find(id="seven-day-forecast-body")
forecast_days = forecast.find_all(class_="tombstone-container")
today = forecast_days[0]  #0 as today is first tag
print(today.prettify())

dayn = today.find(class_="period-name").get_text()
descpr = today.find(class_="short-desc").get_text()
img = today.find("img")
desc = img['title']
temp = today.find(class_="temp").get_text()
print(dayn)
print(descpr)
print(desc)
print(temp)

#extracting info from once from page
#Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
period_tags = forecast.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in forecast.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in forecast.select(".tombstone-container .temp")]
descs = [d["title"] for d in forecast.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)


#using pandas dataframe
import pandas as pd
# making the class with vars
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
weather.to_csv(r'C:\Users\Muneeb\Desktop\export_dataframe.csv' , index = False, header=True)
print(weather)