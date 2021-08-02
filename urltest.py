# import requests
# import os
# import re
# import bs4  # beautifulSoup4
# import urlAvasDemon
from selenium import webdriver

# urlFirstPage = 'http://www.AvasDemon.com/pages.php#0001'
# urlMain = 'http://www.AvasDemon.com'
# filename = 'AvasDemon'
# urlAvasDemon.urlAvasDemon(urlFirstPage, urlMain, filename)

# try:
#     driver = webdriver.Firefox()
# except:
# print("Firefox not found")
try:
    driver = webdriver.Chrome()
except Exception as err:
    print("Chrome not found")
    print("Error:", err)
    exit(999)

# driver.get("https://www.webtoons.com/en/sf/seed/prologue/viewer?title_no=1480&episode_no=1")

# select the next button
# next_button = driver.find_element_by_link_text('Next Episode')
# next_button.click()

# driver.get("https://www.webtoons.com/en/sf/seed/episode-1/viewer?title_no=1480&episode_no=2")

# noinspection PyUnboundLocalVariable
driver.get("http://www.AvasDemon.com")
# print(driver.current_url())
# select the next button
next_button = driver.find_element_by_xpath("//img[@src='latest.png']")
print("next button")
next_button.click()
str = driver.current_url
print(str)
cutstr = str[-4:]
print(cutstr)
