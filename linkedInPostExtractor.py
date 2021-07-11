#importing Selenium Browser
from selenium import webdriver

#give the path of the chromium browser
browser=webdriver.Chrome(executable_path='C:/Users/Vikram/chromedriver.exe')

#Enter the link of the linkedIn Post
postlink=input('Enter the link of the Linked In Post = ')

browser.get(postlink)

k=browser.find_element_by_class_name('share-update-card__update-text')

#Getting the Text
print(k.get_attribute('innerText'))

