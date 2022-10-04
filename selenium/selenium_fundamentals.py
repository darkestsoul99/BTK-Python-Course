from selenium import webdriver
import time 

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("githumb.com-homepage.png")
time.sleep(2)

driver.close()
