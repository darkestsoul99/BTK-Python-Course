from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time 

my_username = "darkestsoul99"
my_password = ""

class GitHub: 
    def __init__(self, username, password) -> None:
        self.browser = webdriver.Chrome()
        self.username = username 
        self.password = password
        self.url = "https://github.com/login"
        self.followers = []

    def signIn(self):
        self.browser.get(self.url)
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id= 'login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id= 'password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[11]").click()
    
    def getFollowers(self): 
        self.browser.get("https://github.com/sadikturan?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(By.XPATH, "/html/body/div[5]/main/div[2]/div/div[2]/div[2]/div/div[5]")
        time.sleep(2)
        for i in items: 
            self.followers.append(i.find_element(By.CSS_SELECTOR, "f4 Link--primary").text)


github = GitHub(my_username, my_password)
github.signIn()
github.getFollowers()
print(github.followers)
        

