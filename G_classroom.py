from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

import time
driver = webdriver.Chrome(executable_path='C:/Users/Muneeb/Downloads/chromedriver_win32/chromedriver.exe') #initilaizes  webdriver
driver.get('https://classroom.google.com/u/0/h')

'''
driver.find_element_by_name("username").send_keys("19I-0591")
driver.find_element_by_name("password").send_keys("Lionzkillermuneeb123")
time.sleep(30) 

driver.find_element_by_id("m_login_signin_submit").click()

time.sleep(10) 
'''