import requests
import os
import re
import bs4  # beautifulSoup4
import urlAvasDemon
from selenium import webdriver

#urlFirstPage = 'http://www.AvasDemon.com/pages.php#0001'
#urlMain = 'http://www.AvasDemon.com'
#filename = 'AvasDemon'
#urlAvasDemon.urlAvasDemon(urlFirstPage, urlMain, filename)

try:
    driver = webdriver.Firefox()
except:
    print("Firefox not found")
    try:
        driver = webdriver.Chrome()
    except:
        print("Chrome not found")
        exit(999)

driver.get("https://www.webtoons.com/en/sf/seed/prologue/viewer?title_no=1480&episode_no=1")

#select the next button
#next_button = driver.find_element_by_link_text('Next Episode')
#next_button.click()

driver.get("https://www.webtoons.com/en/sf/seed/episode-1/viewer?title_no=1480&episode_no=2")


