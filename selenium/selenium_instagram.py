from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
import time 

my_email = "berkekocadere"
my_password = "Themanwhosoldtheworld451"

class Instagram: 
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email 
        self.password = password 
        self.url = "https://www.instagram.com/"

    def signIn(self): 
        self.browser.get(self.url)
        time.sleep(4)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.email)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(4)
    
    def getFollowers(self): 
        time.sleep(4)
        self.browser.get(f"https://www.instagram.com/{self.email}")
        time.sleep(4)
        self.browser.find_element(By.CSS_SELECTOR, 'a[href="/berkekocadere/followers/"]').click()
        time.sleep(4)
        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role='dialog']")
        
        followers = dialog.find_elements(By.CSS_SELECTOR, "div[class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
        followerCount = len(followers)

        print(followerCount)

        action = webdriver.ActionChains(self.browser)

        while True: 
            dialog.click()
            action.scroll_to_element(followers[followerCount-1]).perform()
            time.sleep(4)
            followers = dialog.find_elements(By.CSS_SELECTOR, "div[class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
            newCount = len(followers)

            if followerCount != newCount: 
                followerCount = newCount 
                print(newCount)
            else:
                print(followerCount)
                break 
        
        followerList = []
        for user in followers: 
            link = user.find_element(By.CSS_SELECTOR,"a[role=link]").get_attribute("href")
            followerList.append(link)
            print(link)

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
            
    def followUser(self, username): 
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element(By.CSS_SELECTOR, "div[class='_aacl _aaco _aacw _aad6 _aade']")
        print(followButton.text)
        if followButton.text == "Takip Et": 
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unfollowUser(self, username): 
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        unfollowButton = self.browser.find_element(By.CSS_SELECTOR, "svg[class='_ab6-']")
        print(unfollowButton.text)
        if unfollowButton.get_attribute("aria-label") == "Takiptesin": 
            unfollowButton.click()
            time.sleep(2)
            self.browser.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9-_']").click()
        else:
            print("Takip etmiyorsun")


insta = Instagram(my_email, my_password)
insta.signIn()
time.sleep(2)
insta.getFollowers() 
time.sleep(2)
insta.followUser("Enter username here to follow") 
insta.unfollowUser("Enter username here to unfollow")
