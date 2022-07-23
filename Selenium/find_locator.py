from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("D:\Chrome Driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.youtube.com/')
# search by Name
search = driver.find_element(By.NAME, 'search_query')
search.send_keys('Python Testing For Beginner')
search.submit()

