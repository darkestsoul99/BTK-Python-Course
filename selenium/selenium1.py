# Selenium example 
# 
# Selenium is a web automation module. It can visit a website 
# and interact with it. 

from selenium import webdriver

driver = webdriver.Chrome()

url = "http://sadikturan.com"

driver.get(url)