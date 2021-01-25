from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='C:/Users/Muneeb/Downloads/chromedriver_win32/chromedriver.exe') #initilaizes  webdriver
driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS") #opens the website
more_buttons = driver.find_elements_by_class_name("moreLink")    #finds element by class name
for x in range(len(more_buttons)):
  if more_buttons[x].is_displayed():
      driver.execute_script("arguments[0].click();", more_buttons[x])
      time.sleep(1)

page_source = driver.page_source #source code of page

soup = BeautifulSoup(page_source, 'lxml') #soup initialized
reviews = [] #list
reviews_selector = soup.find_all('div', class_='reviewSelector') #search through div tag with class name reviewselector
for review_selector in reviews_selector:  #search through reviews
    review_div = review_selector.find('div', class_='dyn_full_review')  #search to find full reviews
    if review_div is None:  #if full  review
        review_div = review_selector.find('div', class_='basic_review')  #find basic view
    review = review_div.find('div', class_='entry').find('p').get_text() #search
    review = review.strip()
    reviews.append(review)  #appends reviews list

print(reviews) #prints