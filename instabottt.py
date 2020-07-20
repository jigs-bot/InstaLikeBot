"""I suggest you guys not to copy paste the code from here instead try to write each line
by yourself. writing code make you understand things better"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
import sys             #import Necessary Modules

class InstaBot:  
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #you can Download the driver and locate the driver path as well .
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def closeBrowser(self):
        self.driver.close()

    def login(self):  #Login Function
        driver = self.driver
        driver.get("https://www.instagram.com/") 
        time.sleep(2)
        #Getting Login Button --- You can select element from a web page in other
        #ways also ...
        login_button = driver.find_element_by_tag_name('form')
        login_button.click()
        time.sleep(2)
        user_name = driver.find_element_by_xpath("//input[@name='username']")
        user_name.clear()
        user_name.send_keys(self.username)
        passworword = driver.find_element_by_xpath("//input[@name='password']")
        passworword.clear()
        passworword.send_keys(self.password)
        passworword.send_keys(Keys.RETURN)
        time.sleep(2)

    #functio to like Photos
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
           
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button =driver.find_element_by_xpath('//*[@aria-label="Like"]')
                time.sleep(2)
                like_button.click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1
    
    #Driver Code

if __name__ == "__main__":

    username = "jigyashu.py"
    password = "Yourpassword"
    #Dont try to login my instagram account thinking "yourpassword " is my pswrd

    ig = InstaBot(username, password)
    ig.login()
    #Calling login function

    #change the tags according to your will..
    hashtags = ['jigyashu']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstaBot(username, password)
            ig.login()
