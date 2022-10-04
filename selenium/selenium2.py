from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)
searchInput = driver.find_element(By.NAME, "q") 
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_elements(By.CSS_SELECTOR, "repo-list-item mt-n1 flex-auto f4 text-normal a") 
# We can also use xpath to find element 

for element in result: 
    print(element)

driver.close()