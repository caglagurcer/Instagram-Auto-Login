from selenium import webdriver
import time
import login_info
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()

browser.get("https://www.instagram.com/?hl=en")

time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(login_info.username)
password.send_keys(login_info.password)

time.sleep(1)

loginButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()


time.sleep(5)

profileButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img')
profileButton.click()

time.sleep(2)

prButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]")
prButton.click()

time.sleep(5)

followersButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followersButton.click()

jscommand = """
followers = document.querySelector(".isgrP")
followers.scrollTo(0, followers.scrollHeight)
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

time.sleep(5)

followersList = []

followers = browser.find_elements_by_css_selector(".notranslate._0imsa")


for follower in followers:
    followersList.append(follower.text)

with open("follwers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

browser.close()
